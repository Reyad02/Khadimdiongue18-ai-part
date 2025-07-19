from dotenv import load_dotenv
import json
import os
from prompts import text_extender
from openai import OpenAI


load_dotenv()

# text extender prompt
text_extender_prompt = text_extender(text="Artificial intelligence is changing the way we work and live.",
                                            keywords=["AI", "automation", "technology"],
                                            num_of_results=2,
                                            estimated_result_length=300)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": text_extender_prompt
      }
    ],
    temperature=0.7,
)
    
raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each summary
    for text in parsed["extended_texts"]:
        content = text["content"]
        word_count = len(content.split())
        text["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)
