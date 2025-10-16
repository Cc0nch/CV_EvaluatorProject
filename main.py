# main.py

import google.generativeai as genai
from pathlib import Path
import json

genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel("gemini-1.5-flash")
TEMPERATURE = 0.3

input_dir = Path("sample_inputs")
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

jd_text = (input_dir / "jd.txt").read_text(encoding="utf-8")

cv_files = ["cv1.txt", "cv2.txt", "cv3.txt"]

for cv_file in cv_files:
    cv_text = (input_dir / cv_file).read_text(encoding="utf-8")

    prompt = f"""
Tu esi HR asistents, kurš analizē kandidāta CV un salīdzina to ar darba aprakstu.

Tavs uzdevums ir izvērtēt, cik labi kandidāts atbilst darba aprakstam, un sniegt rezultātu **tikai JSON formātā** ar šādu struktūru:

```json
{{
  "match_score": 0-100,
  "summary": "Īss apraksts, cik labi CV atbilst JD.",
  "strengths": [
    "Galvenās prasmes/pieredze no CV, kas atbilst JD"
  ],
  "missing_requirements": [
    "Svarīgas JD prasības, kas CV nav redzamas"
  ],
  "verdict": "strong match | possible match | not a match"
}}
