import os, json, pathlib, datetime
from openai import OpenAI

ROOT = pathlib.Path(__file__).resolve().parents[1]

def read_text(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")

def write_text(relpath: str, content: str) -> None:
    path = ROOT / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY er ikke satt i miljøvariabler.")

    client = OpenAI(api_key=api_key)

    schema = json.loads(read_text("config/schemas/screening.schema.json"))
    system = read_text("config/prompts/screening.system.md")
    user_tmpl = read_text("config/prompts/screening.user.md")
    capabilities = read_text("index/capabilities.yaml")
    brief = read_text("briefs/tiltak-001.md")

    user = (
        user_tmpl
        .replace("{{CAPABILITIES}}", capabilities)
        .replace("{{BRIEF}}", brief)
    )

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "screening",
                "schema": schema,
                "strict": True
            }
        }
    )

    data = json.loads(resp.output_text)

    today = datetime.date.today().isoformat()
    md = f"""---
id: {data['id']}
dato: {today}
tittel: {data['tittel']}
kilder: {data['kilder']}
status: utkast
kapabiliteter: {data['kapabiliteter']}
fagomrader: {data['fagomrader']}
prinsipper: {data['prinsipper']}
gjenbruk: {data['gjenbruk']}
risiko_nivaa: {data['risiko_nivaa']}
---

## 1. Tiltaksbeskrivelse
{data['tiltaksbeskrivelse']}

## 2. Kontekst og antakelser
{data['antakelser']}

## 3. Vurdering mot kapabiliteter
{data['kapabilitetsvurdering']}

## 4. Vurdering mot prinsipper
{data['prinsippvurdering']}

## 5. Gjenbruk og alternativer
{data['gjenbruk_og_alternativer']}

## 6. Risiko og konsekvenser
{data['risiko_og_konsekvenser']}

## 7. Anbefaling og neste steg
{data['anbefaling']}
"""
    out_path = f"results/screeninger/{today}-{data['id']}.md"
    write_text(out_path, md)

    print(f"Skrev: {out_path}")

if __name__ == "__main__":
    main()