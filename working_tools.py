import os
# import openai
from dotenv import load_dotenv
from prompts import assist_student_chatbot_prompt
# from groq import Groq
from openai import OpenAI

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Initialize student chatbot prompt
chatbot_prompt = assist_student_chatbot_prompt()

def ask_openai(question, message_history):
    message_history.append({"role": "user", "content": question})
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message_history,
            temperature=0.7,
        )
        reply = response.choices[0].message.content.strip()
        message_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print(" Student AI Tutor Chatbot (type 'exit' to quit)\n")

    message_history = [{"role": "system", "content": chatbot_prompt}]

    opening_line = "Hey, my name is Chat AI and I am a professional personal trainer. \nI can help you get muscled up in no time."
    print(f" Chat AI: {opening_line}")
    message_history.append({"role": "assistant", "content": opening_line})

    while True:
        user_input = input("\n You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        answer = ask_openai(user_input, message_history)
        print(f"\n Chat AI: {answer}")

if __name__ == "__main__":
    main()
