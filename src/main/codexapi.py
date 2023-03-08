import os
from dotenv import load_dotenv
import openai

openai.api_key = os.environ.get("CODEX_API_KEY")

def request(prompt):
    body = {
      "model": "code-davinci-002",
      "prompt": prompt,
      "max_tokens": 20,
      "temperature": 0,
      "stop": "}"
    }
    response = openai.Completion.create(**body)
    try:
        result = response["choices"][0]["text"]
        return result
    except:
        return "Can't get the result"


