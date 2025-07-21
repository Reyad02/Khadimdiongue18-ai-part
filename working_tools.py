import os
import json
import uuid
from openai import OpenAI
from dotenv import load_dotenv
from prompts import assist_student_chatbot_prompt  

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HISTORY_FILE = "chat_history.json"

def load_histories():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_histories(histories):
    with open(HISTORY_FILE, "w") as f:
        json.dump(histories, f, indent=2)
        
def retrieve_history(session_id):
    all_histories = load_histories()
    return all_histories.get(session_id, [])

def handle_question(question, session_id=None):
    all_histories = load_histories()

    # Create session ID if not given
    if not session_id:
        session_id = str(uuid.uuid4())
        print(f"Generated new Session ID: {session_id}")

    message_history = retrieve_history(session_id)
    message_history.append({"role": "user", "content": question})
    full_prompt = assist_student_chatbot_prompt(message_history, question)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.7
        )

        raw_json = response.choices[0].message.content.strip()

        try:
            parsed = json.loads(raw_json)
            answer = parsed.get("answer", "No 'answer' key in JSON.")
        except json.JSONDecodeError:
            answer = f"Failed to parse JSON: {raw_json}"

        message_history.append({"role": "assistant", "content": answer})

        all_histories[session_id] = message_history
        save_histories(all_histories)

        return {
            "session_id": session_id,
            "question": question,
            "answer": answer,
            # "raw_json": raw_json,
            # "history": message_history
        }

    except Exception as e:
        return {
            "session_id": session_id,
            "error": str(e)
        }

if __name__ == "__main__":
    question = input("Your question: ").strip()
    session_id = input("Session ID (optional): ").strip() or None

    result = handle_question(question, session_id)
    print(json.dumps(result, indent=2))
