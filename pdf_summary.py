from dotenv import load_dotenv
import os
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
raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each content
    total_words = 0
    for item in parsed["summary"]:
        word_count = len(item["details"].split())
        item["word_count"] = word_count
        total_words += word_count

    parsed["total_word_count"] = total_words

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)



