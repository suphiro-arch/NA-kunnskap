---
title: "Andre ressurser"
weight: 4
description: "Ressurser som foreløpig ikke er plassert i egen ressursmappe med tydelig hovedtype."
hideToc: true
---

# Andre ressurser

Ressurser som foreløpig ikke er plassert i egen ressursmappe med tydelig hovedtype.

Denne siden viser siste registrerte versjon av ressurser i kategorien **Andre ressurser**.

<div class="resource-listing" data-section="andre-ressurser">
  <div class="resource-filters">
    <div class="resource-filters__row">
      <label>Sok <input type="search" class="resource-filter" data-filter="search" placeholder="Navn, ID, type, kapabilitet" /></label>
      <label>Eier <select class="resource-filter" data-filter="owner"><option value="">Alle</option>
        <option value="OPP">OPP</option>
      </select></label>
      <label>Status <select class="resource-filter" data-filter="status"><option value="">Alle</option>
        <option value="Produksjon - modent internasjonalt samhandlingsrammeverk i aktiv bruk for standardisert dokumentutveksling mellom virksomheter.">Produksjon - modent internasjonalt samhandlingsrammeverk i aktiv bruk for standardisert dokumentutveksling mellom virksomheter.</option>
      </select></label>
      <label>Type <select class="resource-filter" data-filter="type"><option value="">Alle</option>
        <option value="Internasjonalt samhandlingsrammeverk">Internasjonalt samhandlingsrammeverk</option>
      </select></label>
      <label>Kapabilitet <select class="resource-filter" data-filter="capability"><option value="">Alle</option>
        <option value="Forvaltningsstandarder">Forvaltningsstandarder</option>
        <option value="Identifisering">Identifisering</option>
        <option value="Meldingsformidling">Meldingsformidling</option>
        <option value="Sikring av informasjonsflyt og datautveksling">Sikring av informasjonsflyt og datautveksling</option>
      </select></label>
    </div>
    <p class="resource-filters__result" data-role="count">Viser 1 av 1 ressurser</p>
  </div>
  <div class="resource-cards">
<article class="resource-card" data-owner="OPP" data-status="Produksjon - modent internasjonalt samhandlingsrammeverk i aktiv bruk for standardisert dokumentutveksling mellom virksomheter." data-type="Internasjonalt samhandlingsrammeverk" data-capabilities="meldingsformidling sikring av informasjonsflyt og datautveksling forvaltningsstandarder identifisering" data-search="peppol edelivery opp-001 opp internasjonal fellesressurs internasjonalt samhandlingsrammeverk peppol edelivery er et internasjonalt samhandlingsrammeverk for sikker og standardisert utveksling av elektroniske dokumenter mellom virksomheter. ressursen er relevant n&#229;r en l&#248;sning trenger et felles transport- og adresseringsm&#248;nster for dokumentutveksling, s&#230;rlig i sammenheng med ehf og andre peppol-baserte... meldingsformidling sikring av informasjonsflyt og datautveksling forvaltningsstandarder identifisering">
  <h2 class="resource-card__title">Peppol eDelivery</h2>
  <p class="resource-card__meta"><strong>Ressurs-ID:</strong> <code>OPP-001</code> | <strong>Siste versjon:</strong> v3 (codex) | <a href="https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/produkter/produktbeskrivelser/11-Peppol-eDelivery-produkt-canvas-v3-codex.md">Markdown</a></p>
  <p class="resource-card__facts"><strong>Eier:</strong> OPP | <strong>Kategori:</strong> Internasjonal fellesressurs | <strong>Type:</strong> Internasjonalt samhandlingsrammeverk</p>
  <p class="resource-card__description">Peppol eDelivery er et internasjonalt samhandlingsrammeverk for sikker og standardisert utveksling av elektroniske dokumenter mellom virksomheter. Ressursen er relevant n&#229;r en l&#248;sning trenger et felles transport- og adresseringsm&#248;nster for dokumentutveksling, s&#230;rlig i sammenheng med EHF og andre Peppol-baserte...</p>
  <p class="resource-card__capabilities"><strong>Kapabiliteter:</strong> <a class="capability-chip" href="../../kapabiliteter/datautveksling-og-integrasjon/meldingsformidling/">Meldingsformidling</a> <a class="capability-chip" href="../../kapabiliteter/informasjonssikkerhet/sikring-av-informasjonsflyt-og-datautveksling/">Sikring av informasjonsflyt og datautveksling</a> <a class="capability-chip" href="../../kapabiliteter/standardisering/forvaltningsstandarder/">Forvaltningsstandarder</a> <span class="capability-chip capability-chip--more">+1</span></p>
  <p class="resource-card__links"><a href="https://peppol.org/">Offisiell lenke</a></p>
</article>
  </div>
  <script>
    (function(){
      var root = document.currentScript.closest(".resource-listing");
      if (!root) { return; }
      var cards = Array.prototype.slice.call(root.querySelectorAll(".resource-card"));
      var count = root.querySelector("[data-role=count]");
      var search = root.querySelector("[data-filter=search]");
      var owner = root.querySelector("[data-filter=owner]");
      var status = root.querySelector("[data-filter=status]");
      var type = root.querySelector("[data-filter=type]");
      var capability = root.querySelector("[data-filter=capability]");
      function norm(v){ return (v || "").toLowerCase(); }
      function apply(){
        var q = norm(search && search.value);
        var o = norm(owner && owner.value);
        var s = norm(status && status.value);
        var t = norm(type && type.value);
        var c = norm(capability && capability.value);
        var visible = 0;
        cards.forEach(function(card){
          var ok = true;
          if (q && card.dataset.search.indexOf(q) === -1) ok = false;
          if (o && norm(card.dataset.owner) !== o) ok = false;
          if (s && norm(card.dataset.status) !== s) ok = false;
          if (t && norm(card.dataset.type) !== t) ok = false;
          if (c && norm(card.dataset.capabilities).indexOf(c) === -1) ok = false;
          card.style.display = ok ? "block" : "none";
          if (ok) visible += 1;
        });
        if (count) { count.textContent = "Viser " + visible + " av " + cards.length + " ressurser"; }
      }
      [search, owner, status, type, capability].forEach(function(el){ if (el) { el.addEventListener("input", apply); el.addEventListener("change", apply); } });
      apply();
    })();
  </script>
</div>
