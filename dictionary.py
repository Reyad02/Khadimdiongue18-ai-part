from dotenv import load_dotenv
# import json
import os
# import re
# from groq import Groq
from prompts import dictionary
from openai import OpenAI

load_dotenv()

# prompt for dictionary 
dictionary_prompt = dictionary(text="friend",
                            num_of_results=2,
                            estimated_result_length=100)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": dictionary_prompt
      }
    ],
    temperature=0.7,
)
    
print(response.choices[0].message.content)

