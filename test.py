from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



response = client.chat.completions.create(
    model="gpt-4.1",  # or "gpt-4o"
    messages=[
        {"role": "user", "content": "Tell me a three sentence bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)
