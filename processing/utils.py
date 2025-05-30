import json

def load_prompt():
    with open("prompts/gemini_prompt.json", "r", encoding="utf-8") as f:
        return json.load(f)["prompt"]
