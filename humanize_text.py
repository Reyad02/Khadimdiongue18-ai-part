from dotenv import load_dotenv
import json
import os
from prompts import humanizer_prompt
from openai import OpenAI

load_dotenv()

# humanize prompt
humanize_prompt = humanizer_prompt(text="Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think, learn, and make decisions. It enables computers to perform tasks that typically require human intelligence, such as understanding natural language, recognizing images, solving problems, making predictions, and adapting to new information. AI systems use algorithms and large datasets to detect patterns, improve accuracy over time, and carry out actions autonomously. From virtual assistants to self-driving cars, AI is transforming industries and how we interact with technology every day.", intensity_level="high",literacy_level="college")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": humanize_prompt
      }
    ],
    temperature=0.7,
)
    
raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    word_count = len(parsed["humanized_text"].split())
    parsed["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)

