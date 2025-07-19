from dotenv import load_dotenv
import json
import os
from prompts import grammar_checker
from openai import OpenAI



load_dotenv()

# grammar checker prompt
grammar_checker_prompt = grammar_checker(
    text="Although it raining heavily, but she still go to office without umbrella.",
    num_of_results=2,
    estimated_result_length=100
)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": grammar_checker_prompt
      }
    ],
    temperature=0.7,
)
    
raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each content
    for content in parsed["corrections"]:
        item = content["content"]
        word_count = len(item.split())
        content["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)
