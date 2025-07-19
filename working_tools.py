import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from prompts import assist_student_chatbot_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize system prompt
message_history = []

print("Ask your academic questions. Type 'exit' to quit.\n")

while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    chatbot_prompt = assist_student_chatbot_prompt(message_history, question)

    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": chatbot_prompt}],
            temperature=0.7,
        )

        raw_reply = response.choices[0].message.content.strip()
        
        # print(raw_reply)
        # {
        # "answer": "Hello! How can I assist you today?"
        # }

        try:
            parsed = json.loads(raw_reply)
            answer = parsed.get("answer", "")
            print("\nAssistant:", answer, "\n")

            message_history.append((question,answer))
            
            # print(message_history)
            # [('hi', 'Hello! How can I help you today?'), ('how are yo?', "I'm just a computer program, so I don't have feelings, but I'm here to help you with any questions you may have. How can I assist you today?"), ('do you know who i am', "As an AI tutor, I don't have the ability to know personal information about individuals. However, I'm here to help you with any questions you have or topics you need assistance with.")]

        except json.JSONDecodeError as e:
            print("Failed to parse JSON:", e)
            print("Raw response:", raw_reply)

    except Exception as e:
        print("⚠️ Error during API call:", str(e))
