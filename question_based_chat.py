import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from extract_data import extract_text_from_pdf
from prompts import build_pdf_qa_prompt

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Extract PDF content
pdf_path = "2507.06213v1.pdf"
pdf_context = extract_text_from_pdf(pdf_path)

# Store chat history
chat_history = []

# Main interaction loop
print("You can now ask questions about the PDF. Type 'exit' to quit.\n")
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

prompt = build_pdf_qa_prompt(pdf_context, chat_history, user_question)

try:
    # Send prompt to OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    raw_output = response.choices[0].message.content.strip()

    # print(raw_output)
    # {
    # "answer": "I'm just a virtual assistant, so I don't have feelings, but thank you for asking! How can I assist you today?"
    # }

    # Try to parse JSON
    try:
        parsed = json.loads(raw_output)
        # print(parsed)
        print("\nAssistant:", parsed["answer"], "\n")
        chat_history.append((user_question, parsed["answer"]))
        
        # print(chat_history)
        # [('hi', 'Hello! How can I assist you today?'), ('how are you', "I'm just a virtual assistant, so I don't have feelings, but thank you for asking! How can I assist you today?")]
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        print("Raw response:", raw_output)
except Exception as e:
        print("⚠️ Error during API call:", str(e))