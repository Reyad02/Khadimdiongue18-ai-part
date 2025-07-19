from dotenv import load_dotenv
import os
from prompts import ai_code_generetor
from openai import OpenAI


load_dotenv()

# ai code generator prompt
ai_code_generetor_prompt = ai_code_generetor("python", "Write a Python function that takes a PDF file path as input and returns the text content of the PDF.")


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": ai_code_generetor_prompt
      }
    ],
    temperature=0.7,
)
    
print(response.choices[0].message.content)



