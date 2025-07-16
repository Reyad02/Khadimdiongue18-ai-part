from dotenv import load_dotenv
# from groq import Groq
# import json
import os
# import re
# from groq import Groq
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
    
print(response.choices[0].message.content)

