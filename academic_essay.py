from dotenv import load_dotenv
import json
import os
from prompts import academic_essay_generator_text
from openai import OpenAI


load_dotenv()

# academic essay generator prompt
academic_essay_generator_prompt = academic_essay_generator_text(title="The Role of Renewable Energy in Combating Climate Change",
                                                keywords=["renewable energy", "carbon emissions", "climate change"],
                                                num_of_results=2,
                                                estimated_result_length=150)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": academic_essay_generator_prompt
      }
    ],
    temperature=0.7,
)
    

raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each essay
    for essay in parsed["essays"]:
        content = essay["content"]
        word_count = len(content.split())
        essay["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)


