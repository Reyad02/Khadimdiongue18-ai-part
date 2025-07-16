from dotenv import load_dotenv
# from groq import Groq
# import json
import os
# import re
# from groq import Groq
from extract_data import extract_text_from_pdf
from prompts import summarize_text, pagewise_summarize_text
from openai import OpenAI
import json

load_dotenv()

# Extract text from the PDF file
pdf_path = "2507.06213v1.pdf"  
pdf_details = extract_text_from_pdf(pdf_path)

# Generate the prompts for pagewise summarization
pagewise_summarize_prompt = pagewise_summarize_text(pdf_details)



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": pagewise_summarize_prompt
      }
    ],
    temperature=0.7,
)
# print(json.loads(response.choices[0].message.content))
print(response.choices[0].message.content)

