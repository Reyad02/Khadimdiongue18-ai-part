from dotenv import load_dotenv
import json
import os
from prompts import paragraph_generator_text
from openai import OpenAI


load_dotenv()

# paragraph generator prompt
paragraph_generator_prompt = paragraph_generator_text(paragraph_description="The Benefits of Meditation for Mental Health", 
                                                keywords=["meditation", "mental clarity", "stress relief", "mindfulness"],
                                                num_of_results=2,
                                                estimated_result_length=100)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": paragraph_generator_prompt
      }
    ],
    temperature=0.7,
)
    
raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each paragraph
    for content in parsed["paragraphs"]:
        item = content["content"]
        word_count = len(item.split())
        content["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)

