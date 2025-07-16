from dotenv import load_dotenv
# from groq import Groq
import os
from extract_data import extract_text_from_pdf
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pdf_path = "2507.06213v1.pdf"
pdf_context = extract_text_from_pdf(pdf_path)

chat_history = []  # list of (question, answer) tuples

print(" You can now ask questions about the PDF. Type 'exit' to quit.\n")
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit"]:
        print(" Goodbye!")
        break
    
    history_text = ""
    for i, (q, a) in enumerate(chat_history):
        history_text += f"User: {q}\nAssistant: {a}\n"



    prompt = f"""
    You are a helpful assistant. Use the following context from a PDF and chat history to answer the question clearly.

     Context:
    \"\"\"{pdf_context}\"\"\"

     Chat History:
    {history_text}

     Question:
    {user_question}

     Answer:
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    answer = response.choices[0].message.content.strip()
    print("\n Assistant:", answer, "\n")

    # Add to history
    chat_history.append((user_question, answer))