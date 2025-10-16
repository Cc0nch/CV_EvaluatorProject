# main.py

import google.generativeai as genai
from pathlib import Path
import json


genai.configure(api_key="YOUR_API_KEY_HERE")


model = genai.GenerativeModel("gemini-2.5-flash")


jd_text = Path("sample_inputs/jd.txt").read_text(encoding="utf-8")


def evaluate_cv(cv_path, output_json_path):
    cv_text = Path(cv_path).read_text(encoding="utf-8")

 
    prompt = f"""
Tu esi HR asistents, kurš analizē kandidāta CV un salīdzina to ar darba aprakstu.

Sniedz rezultātu tikai JSON formātā ar šādu struktūru:
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

---
## Darba apraksts (JD)
{jd_text}

---
## Kandidāta CV
{cv_text}

Lūdzu, atbildi tikai JSON formātā, bez papildu komentāriem.
"""

    
    response = model.generate_content(prompt, generation_config={"temperature": 0.3})

    
    Path(output_json_path).write_text(response.text, encoding="utf-8")
    print(f"✅ Saglabāts: {output_json_path}")


evaluate_cv("sample_inputs/cv1.txt", "outputs/cv1.json")
evaluate_cv("sample_inputs/cv2.txt", "outputs/cv2.json")
evaluate_cv("sample_inputs/cv3.txt", "outputs/cv3.json")

print("🎉 Visi trīs CV ir novērtēti!")

