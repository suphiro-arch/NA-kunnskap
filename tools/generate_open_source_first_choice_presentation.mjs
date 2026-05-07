#!/usr/bin/env node

import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { pathToFileURL } from "node:url";

if (process.env.USERPROFILE) {
  process.env.HOME = process.env.USERPROFILE;
}

const SLIDE_SIZE = { width: 1280, height: 720 };
const ROOT = process.cwd();
const OUTPUT_DIR = path.join(ROOT, "print", "presentasjoner");
const OUTPUT_FILE = path.join(
  OUTPUT_DIR,
  "2026-05-07-apen-kildekode-bor-vare-forstevalg.pptx",
);

const SKILL_DIR = path.join(
  process.env.HOME || process.env.USERPROFILE || ROOT,
  ".codex",
  "plugins",
  "cache",
  "openai-primary-runtime",
  "presentations",
  "26.430.10722",
  "skills",
  "presentations",
);

const CLEANUP_SCRIPT = path.join(SKILL_DIR, "scripts", "cleanup_presentation_workspace.mjs");
const LAYOUT_SCRIPT = path.join(SKILL_DIR, "scripts", "check_layout_quality.mjs");
const ARTIFACT_UTILS = path.join(SKILL_DIR, "scripts", "artifact_tool_utils.mjs");

let createSlideContext;
let ensureArtifactToolWorkspace;
let importArtifactTool;
let saveBlobToFile;

function makeWorkspace() {
  const stamp = "manual-20260507-open-source-first-choice";
  return path.join(os.tmpdir(), "codex-presentations", stamp, "apen-kildekode-forstevalg");
}

function hex(fill) {
  return fill;
}

function runNode(scriptPath, args) {
  const result = spawnSync(process.execPath, [scriptPath, ...args], {
    encoding: "utf8",
    cwd: ROOT,
  });
  const stdout = typeof result.stdout === "string" ? result.stdout.trim() : "";
  const stderr = typeof result.stderr === "string" ? result.stderr.trim() : "";
  if (result.status !== 0) {
    throw new Error(
      [
        `Kommando feilet: node ${path.basename(scriptPath)} ${args.join(" ")}`,
        stdout,
        stderr,
      ]
        .filter(Boolean)
        .join("\n"),
    );
  }
  return stdout;
}

function colors() {
  return {
    paper: hex("#F5F0E8"),
    warm: hex("#E9DDCC"),
    ink: hex("#1C252E"),
    muted: hex("#51606F"),
    teal: hex("#0C8A84"),
    coral: hex("#D46A4C"),
    gold: hex("#D2A64C"),
    moss: hex("#76916D"),
    white: hex("#FFFDF8"),
    line: hex("#D7CBB8"),
    darkPanel: hex("#20313A"),
    darkTeal: hex("#134C52"),
    paleTeal: hex("#DDEFEA"),
    paleCoral: hex("#F3E0D9"),
    paleGold: hex("#F5ECD5"),
    paleMoss: hex("#E4EADB"),
  };
}

function addBand(ctx, slide, { x, y, w, h, fill, name }) {
  return ctx.addShape(slide, {
    x,
    y,
    w,
    h,
    fill,
    line: ctx.line(fill, 0),
    name,
  });
}

function addText(ctx, slide, options) {
  return ctx.addText(slide, {
    color: colors().ink,
    face: ctx.fonts.body,
    ...options,
  });
}

function addKicker(ctx, slide, label, markerFill, index = "01") {
  const y = 36;
  addBand(ctx, slide, {
    x: 72,
    y: y + 6,
    w: 20,
    h: 20,
    fill: markerFill,
    name: `kicker-${index}-marker`,
  });
  addText(ctx, slide, {
    x: 102,
    y,
    w: 240,
    h: 34,
    text: label.toUpperCase(),
    fontSize: 14,
    color: colors().muted,
    face: "Aptos",
    name: `kicker-${index}-label`,
    valign: "middle",
  });
}

function addPageNumber(ctx, slide, value) {
  addText(ctx, slide, {
    x: 1160,
    y: 668,
    w: 48,
    h: 24,
    text: String(value).padStart(2, "0"),
    fontSize: 12,
    color: colors().muted,
    align: "right",
  });
}

function addFooter(ctx, slide, text, page) {
  addBand(ctx, slide, {
    x: 72,
    y: 652,
    w: 1136,
    h: 1,
    fill: colors().line,
  });
  addText(ctx, slide, {
    x: 72,
    y: 664,
    w: 980,
    h: 22,
    text,
    fontSize: 11,
    color: colors().muted,
  });
  addPageNumber(ctx, slide, page);
}

function addTitleBlock(ctx, slide, { kicker, claim, support, page, kickerFill }) {
  addKicker(ctx, slide, kicker, kickerFill);
  addText(ctx, slide, {
    x: 72,
    y: 84,
    w: 760,
    h: 72,
    text: claim,
    fontSize: 31,
    face: "Georgia",
    color: colors().ink,
  });
  if (support) {
    addText(ctx, slide, {
      x: 72,
      y: 170,
      w: 760,
      h: 54,
      text: support,
      fontSize: 17,
      color: colors().muted,
    });
  }
}

function addPill(ctx, slide, { x, y, w, text, fill, color = colors().ink }) {
  addBand(ctx, slide, { x, y, w, h: 34, fill });
  addText(ctx, slide, {
    x: x + 14,
    y: y + 3,
    w: w - 28,
    h: 28,
    text,
    fontSize: 14,
    color,
    valign: "middle",
  });
}

function addCard(ctx, slide, { x, y, w, h, fill, title, body, titleColor = colors().ink }) {
  addBand(ctx, slide, { x, y, w, h, fill });
  addText(ctx, slide, {
    x: x + 18,
    y: y + 18,
    w: w - 36,
    h: 36,
    text: title,
    fontSize: 20,
    face: "Georgia",
    color: titleColor,
  });
  addText(ctx, slide, {
    x: x + 18,
    y: y + 64,
    w: w - 36,
    h: h - 82,
    text: body,
    fontSize: 15,
    color: titleColor === colors().white ? colors().paper : colors().muted,
  });
}

async function slide01(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, {
    ...baseCtx,
    slideNumber: 1,
  });
  slide.background.fill = colors().paper;

  addKicker(ctx, slide, "Tese", colors().teal);
  addText(ctx, slide, {
    x: 72,
    y: 94,
    w: 660,
    h: 148,
    text: "Åpen kildekode\nbør være førstevalg.",
    fontSize: 34,
    face: "Georgia",
    color: colors().ink,
  });
  addText(ctx, slide, {
    x: 72,
    y: 246,
    w: 560,
    h: 84,
    text: "Ikke som ideologi, men som standardbeslutning når offentlig sektor skal bygge, kjøpe eller videreutvikle digitale løsninger.",
    fontSize: 19,
    color: colors().muted,
  });

  addBand(ctx, slide, { x: 72, y: 384, w: 450, h: 2, fill: colors().line });
  addPill(ctx, slide, {
    x: 72,
    y: 404,
    w: 182,
    text: "Mer gjenbruk",
    fill: colors().paleTeal,
  });
  addPill(ctx, slide, {
    x: 264,
    y: 404,
    w: 184,
    text: "Mindre innlåsing",
    fill: colors().paleCoral,
  });
  addPill(ctx, slide, {
    x: 72,
    y: 448,
    w: 184,
    text: "Bedre etterprøvbarhet",
    fill: colors().paleGold,
  });
  addPill(ctx, slide, {
    x: 266,
    y: 448,
    w: 160,
    text: "Høyere tempo",
    fill: colors().paleMoss,
  });

  addBand(ctx, slide, {
    x: 820,
    y: 84,
    w: 350,
    h: 520,
    fill: colors().darkPanel,
  });
  addCard(ctx, slide, {
    x: 850,
    y: 116,
    w: 290,
    h: 132,
    fill: colors().darkTeal,
    title: "Styring",
    body: "Koden kan vurderes, forbedres, flyttes og videreføres uten å starte på nytt hver gang avtalen eller leverandøren endrer seg.",
    titleColor: colors().white,
  });
  addCard(ctx, slide, {
    x: 850,
    y: 268,
    w: 290,
    h: 132,
    fill: colors().teal,
    title: "Gjenbruk",
    body: "Offentlig finansiert utvikling blir et felles utgangspunkt som andre virksomheter kan tilpasse, ikke bare et lokalt sluttprodukt.",
    titleColor: colors().white,
  });
  addCard(ctx, slide, {
    x: 850,
    y: 420,
    w: 290,
    h: 132,
    fill: colors().coral,
    title: "Tempo",
    body: "Utvikling går raskere når vi kan bygge videre på eksisterende komponenter, praksis og feilrettinger i stedet for å kjøpe alt på nytt.",
    titleColor: colors().white,
  });

  addFooter(
    ctx,
    slide,
    "Syntese av offentlige kilder per 7. mai 2026: European Commission, Interoperable Europe, Regjeringen.no og NAV.",
    1,
  );
  return slide;
}

async function slide02(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 2 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Hvorfor nå",
    claim: "Offentlig sektor trenger mer gjenbruk og mindre parallelle innlåsingseffekter.",
    support: "Tre samtidige drivere peker i samme retning: styringsbehov, gjenbrukskrav og økende forventning om digital autonomi.",
    page: 2,
    kickerFill: colors().gold,
  });

  const columns = [
    {
      x: 72,
      fill: colors().paleTeal,
      accent: colors().teal,
      icon: "scale",
      title: "Offentlige penger",
      body: "Når skattefinansiert utvikling låses til én leverandør eller ett lukket produktspor, mister forvaltningen både læring og viderebruk.",
    },
    {
      x: 454,
      fill: colors().paleGold,
      accent: colors().gold,
      icon: "database",
      title: "Gjenbrukspress",
      body: "Digitaliseringsrundskrivet fra 27. mai 2025 løfter gjenbruk og viderebruk av informasjon som et eksplisitt styringskrav i offentlig sektor.",
    },
    {
      x: 836,
      fill: colors().paleCoral,
      accent: colors().coral,
      icon: "compass",
      title: "Strategisk autonomi",
      body: "EU-kommisjonen knytter åpen kildekode til deling, gjenbruk, digital autonomi og bedre offentlige tjenester i sin åpne programvarestrategi.",
    },
  ];

  for (const [index, column] of columns.entries()) {
    addBand(ctx, slide, {
      x: column.x,
      y: 248,
      w: 330,
      h: 310,
      fill: column.fill,
    });
    addText(ctx, slide, {
      x: column.x + 20,
      y: 264,
      w: 40,
      h: 42,
      text: `0${index + 1}`,
      fontSize: 30,
      face: "Georgia",
      color: column.accent,
    });
    await ctx.addLucideIcon(slide, {
      icon: column.icon,
      x: column.x + 250,
      y: 268,
      w: 44,
      h: 44,
      color: column.accent,
    });
    addText(ctx, slide, {
      x: column.x + 20,
      y: 322,
      w: 260,
      h: 36,
      text: column.title,
      fontSize: 22,
      face: "Georgia",
      color: colors().ink,
    });
    addText(ctx, slide, {
      x: column.x + 20,
      y: 370,
      w: 286,
      h: 148,
      text: column.body,
      fontSize: 16,
      color: colors().muted,
    });
    addBand(ctx, slide, {
      x: column.x + 20,
      y: 528,
      w: 290,
      h: 6,
      fill: column.accent,
    });
  }

  addFooter(
    ctx,
    slide,
    "Kilder: Digitaliseringsrundskrivet 2025 (Regjeringen.no) og Open source software strategy (European Commission).",
    2,
  );
  return slide;
}

async function slide03(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 3 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Beslutningslogikk",
    claim: "Når koden kan deles, blir investeringer en fellesbygget kapasitet.",
    support: "Forskjellen handler ikke bare om lisenspris. Den handler om hvem som kontrollerer endringstakt, flyttbarhet og læring over tid.",
    page: 3,
    kickerFill: colors().coral,
  });

  addBand(ctx, slide, { x: 72, y: 236, w: 760, h: 344, fill: colors().white });

  const colX = [72, 316, 520, 694];
  const colW = [244, 204, 174, 138];
  const headers = [
    "Vurdering",
    "Åpen kildekode som førstevalg",
    "Proprietær standard",
    "Hva avgjør?",
  ];
  for (let i = 0; i < headers.length; i += 1) {
    addBand(ctx, slide, {
      x: colX[i],
      y: 236,
      w: colW[i],
      h: 56,
      fill: i === 1 ? colors().teal : i === 2 ? colors().warm : colors().ink,
    });
    addText(ctx, slide, {
      x: colX[i] + 16,
      y: 248,
      w: colW[i] - 32,
      h: 32,
      text: headers[i],
      fontSize: 14,
      color: colors().white,
      valign: "middle",
    });
  }

  const rows = [
    ["Strategisk kontroll", "Høy", "Middels til lav", "Tilgang til kode og rett til videreutvikling"],
    ["Gjenbruk på tvers", "Sterk", "Avhenger av avtale", "Delbarhet og lisensvilkår"],
    ["Leverandørfleksibilitet", "Høyere", "Lavere", "Mulighet for flere drifts- og utviklingsmiljøer"],
    ["Etterprøvbarhet", "Direkte", "Indirekte", "Innsyn i kode, sikkerhet og avhengigheter"],
    ["Exit-kostnad", "Lavere over tid", "Ofte høy", "Hvor tungt det er å bytte løsning eller partner"],
  ];

  rows.forEach((row, rowIndex) => {
    const y = 292 + rowIndex * 56;
    const fills = [
      rowIndex % 2 === 0 ? colors().paleGold : colors().white,
      rowIndex % 2 === 0 ? colors().paleTeal : colors().white,
      rowIndex % 2 === 0 ? colors().paleCoral : colors().white,
      rowIndex % 2 === 0 ? colors().paleMoss : colors().white,
    ];
    for (let i = 0; i < row.length; i += 1) {
      addBand(ctx, slide, {
        x: colX[i],
        y,
        w: colW[i],
        h: 56,
        fill: fills[i],
      });
      addText(ctx, slide, {
        x: colX[i] + 16,
        y: y + 10,
        w: colW[i] - 32,
        h: 36,
        text: row[i],
        fontSize: i === 3 ? 13 : 15,
        color: i === 0 ? colors().ink : colors().muted,
        valign: "middle",
      });
    }
  });

  addBand(ctx, slide, {
    x: 874,
    y: 236,
    w: 334,
    h: 344,
    fill: colors().darkPanel,
  });
  addText(ctx, slide, {
    x: 904,
    y: 266,
    w: 274,
    h: 42,
    text: "Poenget",
    fontSize: 28,
    face: "Georgia",
    color: colors().white,
  });
  addText(ctx, slide, {
    x: 904,
    y: 326,
    w: 274,
    h: 164,
    text: "Førstevalg betyr at åpen kildekode vurderes som normaltilfellet.\n\nAvvik kan være riktig, men må da begrunnes med funksjon, risiko eller marked, ikke med vane.",
    fontSize: 17,
    color: colors().paper,
  });
  addPill(ctx, slide, {
    x: 904,
    y: 512,
    w: 206,
    text: "Standard: åpent først",
    fill: colors().teal,
    color: colors().white,
  });

  addFooter(
    ctx,
    slide,
    "Kildegrunnlag: European Commission 'Think Open' og Digitaliseringsrundskrivet 2025. Tabellen er en syntese.",
    3,
  );
  return slide;
}

async function slide04(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 4 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Kumulativ effekt",
    claim: "Åpen kildekode gjør offentlig finansiert utvikling kumulativ.",
    support: "Samme investering kan forbedres, deles og tilpasses flere ganger uten at hver virksomhet må kjøpe hele læringsløpet på nytt.",
    page: 4,
    kickerFill: colors().moss,
  });

  const stages = [
    { x: 88, title: "1. Bygg", body: "Én virksomhet utvikler en løsning for et konkret behov.", fill: colors().paleCoral },
    { x: 356, title: "2. Del", body: "Kode, erfaringer og avhengigheter kan publiseres og dokumenteres åpent.", fill: colors().paleTeal },
    { x: 624, title: "3. Tilpass", body: "Andre kan gjenbruke og tilpasse uten å starte fra blanke ark.", fill: colors().paleGold },
    { x: 892, title: "4. Forbedre", body: "Feilrettinger og forbedringer kan føres tilbake til samme spor.", fill: colors().paleMoss },
  ];

  stages.forEach((stage, index) => {
    addBand(ctx, slide, {
      x: stage.x,
      y: 298,
      w: 220,
      h: 176,
      fill: stage.fill,
    });
    addText(ctx, slide, {
      x: stage.x + 18,
      y: 318,
      w: 184,
      h: 32,
      text: stage.title,
      fontSize: 24,
      face: "Georgia",
    });
    addText(ctx, slide, {
      x: stage.x + 18,
      y: 366,
      w: 184,
      h: 78,
      text: stage.body,
      fontSize: 15,
      color: colors().muted,
    });
    if (index < stages.length - 1) {
      addBand(ctx, slide, {
        x: stage.x + 220,
        y: 378,
        w: 34,
        h: 4,
        fill: colors().ink,
      });
      addBand(ctx, slide, {
        x: stage.x + 248,
        y: 370,
        w: 10,
        h: 20,
        fill: colors().ink,
      });
    }
  });

  addBand(ctx, slide, { x: 198, y: 520, w: 768, h: 4, fill: colors().ink });
  addBand(ctx, slide, { x: 198, y: 520, w: 4, h: 40, fill: colors().ink });
  addBand(ctx, slide, { x: 962, y: 520, w: 4, h: 40, fill: colors().ink });
  addBand(ctx, slide, { x: 198, y: 556, w: 760, h: 4, fill: colors().ink });
  addBand(ctx, slide, { x: 188, y: 548, w: 10, h: 20, fill: colors().ink });
  addText(ctx, slide, {
    x: 370,
    y: 568,
    w: 420,
    h: 26,
    text: "Tilbakeføring gir felles læring og lavere total endringskostnad.",
    fontSize: 14,
    color: colors().muted,
    align: "center",
  });

  addFooter(
    ctx,
    slide,
    "Logikken samsvarer med EU OSS Catalogue og EU OSPO Network: deling, gjenbruk og forbedring på tvers av offentlige miljøer.",
    4,
  );
  return slide;
}

async function slide05(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 5 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Sikkerhet og kvalitet",
    claim: "Åpenhet flytter sikkerhet fra tillit alene til etterprøvbarhet i praksis.",
    support: "Åpen kildekode er ikke sikkert av seg selv, men den gjør det enklere å inspisere, teste, dokumentere og bytte ut svake deler tidligere.",
    page: 5,
    kickerFill: colors().teal,
  });

  const boxes = [
    {
      x: 72,
      y: 258,
      fill: colors().paleTeal,
      title: "Åpen inspeksjon",
      body: "Flere kan vurdere kode, konfigurasjon og arkitekturvalg. Det senker terskelen for tidlig oppdagelse av svake mønstre.",
      icon: "search-check",
      accent: colors().teal,
    },
    {
      x: 656,
      y: 258,
      fill: colors().paleCoral,
      title: "Dokumenterte avhengigheter",
      body: "SBOM, byggkjeder og lisensbilde blir enklere å følge når miljøet ikke er en lukket svart boks.",
      icon: "package-search",
      accent: colors().coral,
    },
    {
      x: 72,
      y: 438,
      fill: colors().paleGold,
      title: "Raskere feilretting",
      body: "Når koden kan justeres av flere enn leverandøren alene, blir handlingsrommet større i kritiske situasjoner.",
      icon: "shield-check",
      accent: colors().gold,
    },
    {
      x: 656,
      y: 438,
      fill: colors().paleMoss,
      title: "Reell exit-mulighet",
      body: "Dersom kvalitet eller tempo svikter, kan organisasjonen flytte drift eller videreutvikling uten å kassere hele investeringen.",
      icon: "door-open",
      accent: colors().moss,
    },
  ];

  for (const box of boxes) {
    addBand(ctx, slide, {
      x: box.x,
      y: box.y,
      w: 552,
      h: 142,
      fill: box.fill,
    });
    await ctx.addLucideIcon(slide, {
      icon: box.icon,
      x: box.x + 24,
      y: box.y + 24,
      w: 32,
      h: 32,
      color: box.accent,
    });
    addText(ctx, slide, {
      x: box.x + 70,
      y: box.y + 18,
      w: 430,
      h: 30,
      text: box.title,
      fontSize: 22,
      face: "Georgia",
    });
    addText(ctx, slide, {
      x: box.x + 24,
      y: box.y + 62,
      w: 504,
      h: 58,
      text: box.body,
      fontSize: 16,
      color: colors().muted,
    });
  }

  addFooter(
    ctx,
    slide,
    "Kilder: European Commission Open Source Strategy og EU-FOSSA-beskrivelsen av FOSS-sikkerhet og samfunnsgevinst.",
    5,
  );
  return slide;
}

async function slide06(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 6 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Praksis i dag",
    claim: "Praksisen finnes allerede; utfordringen er å gjøre den til styrende standard.",
    support: "Både norske og europeiske miljøer behandler åpen kildekode som et virkemiddel for samarbeid, gjenbruk og bedre offentlige tjenester.",
    page: 6,
    kickerFill: colors().gold,
  });

  addBand(ctx, slide, { x: 72, y: 244, w: 500, h: 332, fill: colors().darkPanel });
  addText(ctx, slide, {
    x: 102,
    y: 278,
    w: 340,
    h: 90,
    text: "“We build our software in the open.”",
    fontSize: 28,
    face: "Georgia",
    color: colors().white,
  });
  addText(ctx, slide, {
    x: 102,
    y: 382,
    w: 370,
    h: 96,
    text: "NAV begrunner dette med at løsningene er finansiert av fellesskapet, og at åpen kildekode styrker samarbeid og produktkvalitet.",
    fontSize: 17,
    color: colors().paper,
  });
  addPill(ctx, slide, {
    x: 102,
    y: 506,
    w: 210,
    text: "Eksempel: NAV på GitHub",
    fill: colors().teal,
    color: colors().white,
  });

  addBand(ctx, slide, { x: 624, y: 244, w: 584, h: 332, fill: colors().white });
  addText(ctx, slide, {
    x: 654,
    y: 268,
    w: 500,
    h: 30,
    text: "Europeisk retning",
    fontSize: 24,
    face: "Georgia",
  });

  const steps = [
    {
      y: 318,
      title: "EU OSS Catalogue",
      body: "Føderert katalog som samler åpne løsninger fra offentlige kataloger gjennom åpne API-er for å styrke gjenbruk.",
      fill: colors().paleTeal,
    },
    {
      y: 410,
      title: "EU OSPO Network",
      body: "Nettverk som skal fremme åpne løsninger i offentlig sektor og støtte at offentlig finansiert programvare publiseres som åpen kildekode.",
      fill: colors().paleGold,
    },
    {
      y: 502,
      title: "Kommisjonens strategi",
      body: "Knytter åpen kildekode til deling, kontroll, sikkerhet og digital autonomi i egne offentlige tjenester.",
      fill: colors().paleCoral,
    },
  ];

  for (const step of steps) {
    addBand(ctx, slide, { x: 654, y: step.y, w: 510, h: 70, fill: step.fill });
    addText(ctx, slide, {
      x: 676,
      y: step.y + 12,
      w: 210,
      h: 24,
      text: step.title,
      fontSize: 18,
      face: "Georgia",
    });
    addText(ctx, slide, {
      x: 676,
      y: step.y + 36,
      w: 454,
      h: 22,
      text: step.body,
      fontSize: 13,
      color: colors().muted,
    });
  }

  addFooter(
    ctx,
    slide,
    "Kilder: github.com/navikt, Interoperable Europe (EU OSS Catalogue og EU OSPO Network), European Commission.",
    6,
  );
  return slide;
}

async function slide07(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 7 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Styrt avvik",
    claim: "Førstevalg er ikke tvang; avvik må begrunnes og dokumenteres.",
    support: "Åpen kildekode er riktig som standard hvis vi samtidig er tydelige på når et avvik faktisk er fornuftig.",
    page: 7,
    kickerFill: colors().coral,
  });

  addBand(ctx, slide, { x: 72, y: 254, w: 744, h: 284, fill: colors().white });
  addPill(ctx, slide, {
    x: 108,
    y: 278,
    w: 192,
    text: "Utgangspunkt",
    fill: colors().darkPanel,
    color: colors().white,
  });
  addText(ctx, slide, {
    x: 108,
    y: 322,
    w: 192,
    h: 60,
    text: "Velg åpen kildekode først.",
    fontSize: 22,
    face: "Georgia",
  });

  const gates = [
    {
      x: 314,
      fill: colors().paleTeal,
      title: "Gate 1",
      body: "Dekker åpne alternativer funksjon og modenhet godt nok?",
    },
    {
      x: 490,
      fill: colors().paleGold,
      title: "Gate 2",
      body: "Kan løsning, kode og avhengigheter forvaltes uten uforholdsmessig risiko?",
    },
    {
      x: 666,
      fill: colors().paleCoral,
      title: "Gate 3",
      body: "Hvis svaret er nei: er avviket tidsavgrenset, dokumentert og revurderbart?",
    },
  ];
  gates.forEach((gate, index) => {
    addBand(ctx, slide, { x: gate.x, y: 300, w: 140, h: 192, fill: gate.fill });
    addText(ctx, slide, {
      x: gate.x + 18,
      y: 320,
      w: 104,
      h: 24,
      text: gate.title,
      fontSize: 18,
      face: "Georgia",
    });
    addText(ctx, slide, {
      x: gate.x + 18,
      y: 360,
      w: 102,
      h: 98,
      text: gate.body,
      fontSize: 14,
      color: colors().muted,
    });
    if (index < gates.length - 1) {
      addBand(ctx, slide, { x: gate.x + 140, y: 388, w: 18, h: 4, fill: colors().ink });
      addBand(ctx, slide, { x: gate.x + 154, y: 380, w: 8, h: 20, fill: colors().ink });
    }
  });

  addBand(ctx, slide, { x: 854, y: 254, w: 354, h: 284, fill: colors().darkPanel });
  addText(ctx, slide, {
    x: 884,
    y: 286,
    w: 290,
    h: 34,
    text: "Typiske avvik",
    fontSize: 24,
    face: "Georgia",
    color: colors().white,
  });
  addText(ctx, slide, {
    x: 884,
    y: 338,
    w: 286,
    h: 148,
    text: "• Særskilt funksjonalitet uten troverdige åpne alternativer\n• Tydelig regulatorisk eller sikkerhetsmessig binding\n• Midlertidige avvik mens en åpen løsning modnes\n\nPoenget er å kunne forklare avviket, ikke å la det bli standard av vane.",
    fontSize: 16,
    color: colors().paper,
  });

  addFooter(
    ctx,
    slide,
    "Anbefalt styringsprinsipp: åpent først, avvik bare med tydelig begrunnelse, plan og ny vurdering.",
    7,
  );
  return slide;
}

async function slide08(presentation, baseCtx) {
  const slide = presentation.slides.add();
  const ctx = createSlideContext(baseCtx.artifact, { ...baseCtx, slideNumber: 8 });
  slide.background.fill = colors().paper;

  addTitleBlock(ctx, slide, {
    kicker: "Hva vi gjør",
    claim: "Det vanskeligste er ikke teknologien, men å endre standardbeslutningen.",
    support: "Start med noen få konkrete grep som gjør åpen kildekode til en styrt del av anskaffelse, utvikling og forvaltning.",
    page: 8,
    kickerFill: colors().moss,
  });

  addBand(ctx, slide, { x: 72, y: 256, w: 1136, h: 220, fill: colors().white });
  const roadmap = [
    { x: 100, title: "0-30 dager", body: "Bestem prinsipp: åpen kildekode er førstevalg i nye vurderinger." },
    { x: 376, title: "30-60 dager", body: "Legg inn krav om exit, kildekode, lisens og dokumentasjon i anskaffelser." },
    { x: 652, title: "60-90 dager", body: "Velg 3-5 kandidater der åpne komponenter eller publisering gir rask gevinst." },
    { x: 928, title: "90+ dager", body: "Etabler lett OSPO-funksjon, publiseringspraksis og læringssløyfe." },
  ];

  roadmap.forEach((item, index) => {
    addBand(ctx, slide, {
      x: item.x,
      y: 302,
      w: 220,
      h: 126,
      fill: index % 2 === 0 ? colors().paleTeal : colors().paleGold,
    });
    addText(ctx, slide, {
      x: item.x + 18,
      y: 320,
      w: 180,
      h: 24,
      text: item.title,
      fontSize: 20,
      face: "Georgia",
    });
    addText(ctx, slide, {
      x: item.x + 18,
      y: 356,
      w: 182,
      h: 52,
      text: item.body,
      fontSize: 14,
      color: colors().muted,
    });
    if (index < roadmap.length - 1) {
      addBand(ctx, slide, { x: item.x + 220, y: 362, w: 34, h: 4, fill: colors().ink });
      addBand(ctx, slide, { x: item.x + 248, y: 354, w: 10, h: 20, fill: colors().ink });
    }
  });

  addBand(ctx, slide, { x: 72, y: 506, w: 780, h: 108, fill: colors().darkPanel });
  addText(ctx, slide, {
    x: 102,
    y: 526,
    w: 712,
    h: 70,
    text: "Hvis vi mener alvor med gjenbruk, digital autonomi og bedre forvaltning av offentlige investeringer, bør åpen kildekode være standardsporet.",
    fontSize: 22,
    face: "Georgia",
    color: colors().white,
  });

  addBand(ctx, slide, { x: 886, y: 506, w: 322, h: 108, fill: colors().paleCoral });
  addText(ctx, slide, {
    x: 908,
    y: 526,
    w: 270,
    h: 64,
    text: "Spørsmålet er ikke om åpent alltid er riktig.\nSpørsmålet er hvorfor lukket skal være normalen.",
    fontSize: 16,
    color: colors().ink,
  });

  addFooter(
    ctx,
    slide,
    "Oppsummering: åpent først som styringsregel, med dokumenterte avvik når det er saklig nødvendig.",
    8,
  );
  return slide;
}

async function exportDeck(artifact, presentation, outPath, previewDir, layoutDir) {
  const slides = [];
  for (let index = 0; index < presentation.slides.count; index += 1) {
    const slide = presentation.slides.getItem(index);
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    const pngPath = path.join(previewDir, `slide-${String(index + 1).padStart(2, "0")}.png`);
    await saveBlobToFile(png, pngPath);

    const layoutBlob = await presentation.export({ slide, format: "layout" });
    const layoutPath = path.join(layoutDir, `slide-${String(index + 1).padStart(2, "0")}.layout.json`);
    await fs.writeFile(layoutPath, await layoutBlob.text(), "utf8");
    slides.push({ pngPath, layoutPath });
  }

  const { PresentationFile } = artifact;
  const file = await PresentationFile.exportPptx(presentation);
  await file.save(outPath);
  return slides;
}

async function main() {
  ({
    createSlideContext,
    ensureArtifactToolWorkspace,
    importArtifactTool,
    saveBlobToFile,
  } = await import(pathToFileURL(ARTIFACT_UTILS).href));

  const workspace = makeWorkspace();
  const previewDir = path.join(workspace, "preview");
  const layoutDir = path.join(workspace, "layout");

  await fs.mkdir(OUTPUT_DIR, { recursive: true });
  await fs.mkdir(previewDir, { recursive: true });
  await fs.mkdir(layoutDir, { recursive: true });

  await ensureArtifactToolWorkspace(workspace);
  const artifact = await importArtifactTool(workspace);
  const { Presentation } = artifact;
  const presentation = Presentation.create({ slideSize: SLIDE_SIZE });

  const baseCtx = {
    artifact,
    slideSize: SLIDE_SIZE,
    outputDir: OUTPUT_DIR,
    assetDir: path.join(workspace, "assets"),
    workspaceDir: workspace,
  };

  await slide01(presentation, baseCtx);
  await slide02(presentation, baseCtx);
  await slide03(presentation, baseCtx);
  await slide04(presentation, baseCtx);
  await slide05(presentation, baseCtx);
  await slide06(presentation, baseCtx);
  await slide07(presentation, baseCtx);
  await slide08(presentation, baseCtx);

  await exportDeck(artifact, presentation, OUTPUT_FILE, previewDir, layoutDir);

  const stat = await fs.stat(OUTPUT_FILE);
  if (stat.size <= 0) {
    throw new Error(`Tom presentasjonsfil: ${OUTPUT_FILE}`);
  }

  try {
    runNode(LAYOUT_SCRIPT, ["--layout", layoutDir, "--warn-only"]);
  } catch (error) {
    console.warn(String(error.message || error));
  }

  try {
    runNode(CLEANUP_SCRIPT, ["--workspace", workspace, "--output-dir", OUTPUT_DIR]);
  } catch (error) {
    console.warn(String(error.message || error));
  }

  console.log(
    JSON.stringify(
      {
        output: OUTPUT_FILE,
        size: stat.size,
        slideCount: presentation.slides.count,
      },
      null,
      2,
    ),
  );
}

main().catch((error) => {
  console.error(error.stack || error.message || String(error));
  process.exit(1);
});
