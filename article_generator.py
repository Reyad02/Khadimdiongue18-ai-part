from dotenv import load_dotenv
# from groq import Groq
# import json
import os
# import re
# from groq import Groq
from prompts import article_generator_text
from openai import OpenAI


load_dotenv()

# article generator prompt
article_generator_prompt = article_generator_text(title="The Benefits of Meditation for Mental Health", 
                                                keywords=["meditation", "mental clarity", "stress relief", "mindfulness"],
                                                num_of_results=2,
                                                estimated_result_length=100)


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
    
print(response.choices[0].message.content)

