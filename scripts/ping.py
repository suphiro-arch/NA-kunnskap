import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

resp = client.responses.create(
    model="gpt-4.1-mini",
    input="Svar med kun teksten: OK"
)

print(resp.output_text)