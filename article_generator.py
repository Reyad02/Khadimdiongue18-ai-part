from dotenv import load_dotenv
import json
import os
from prompts import article_generator_text
from openai import OpenAI


load_dotenv()

# article generator prompt
article_generator_prompt = article_generator_text(title="The Benefits of Meditation for Mental Health", 
                                                keywords=["meditation", "mental clarity", "stress relief", "mindfulness"],
                                                num_of_results=2,
                                                estimated_result_length=800)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": article_generator_prompt
      }
    ],
    temperature=0.7,
)
    

raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each article
    for article in parsed["articles"]:
        content = article["content"]
        word_count = len(content.split())
        article["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)

