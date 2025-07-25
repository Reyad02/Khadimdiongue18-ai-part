from dotenv import load_dotenv
import json
from openai import OpenAI
import os
from prompts import summarize_text_2nd_grade


load_dotenv()

text_to_summarize = """Artificial Intelligence (AI) is reshaping the modern workplace. From automating repetitive tasks to enhancing decision-making, AI technologies are now widely used across industries like healthcare, finance, manufacturing, and customer service.

One of AI’s most noticeable effects is the automation of routine tasks. Jobs such as data entry, meeting scheduling, and basic customer support are increasingly handled by intelligent systems. This allows human employees to focus on tasks that require creativity, problem-solving, and emotional intelligence—areas where AI still falls short.

However, automation brings challenges too. Many workers fear job loss as machines take over certain roles, especially low-skill ones. While some jobs will disappear, new opportunities are also emerging. Roles related to AI oversight, ethical decision-making, and data analysis are in high demand. This shift highlights the need for employees to learn new skills and adapt to changing job landscapes.

AI also helps businesses make smarter decisions. Machine learning models can quickly analyze large amounts of data to find patterns that humans might miss. These insights improve planning, product recommendations, and even risk management. Instead of replacing human judgment, AI supports it—making teams faster and more accurate.

In communication, AI-powered tools like chatbots and virtual assistants are streamlining how teams work, especially in remote and hybrid settings. These tools can summarize meetings, suggest tasks, and keep projects on track.

Still, AI raises important ethical concerns. Issues like privacy, bias in algorithms, and lack of transparency can’t be ignored. Companies need to develop strong ethical guidelines and ensure AI tools are used responsibly.

In summary, AI is transforming work—bringing both opportunities and challenges. Success in this new era depends on continuous learning, ethical awareness, and using AI to complement—not replace—human skills."""


# prompt for summary for 2nd grader 
summarize_text_2nd_grade_prompt = summarize_text_2nd_grade(text=text_to_summarize,
                                                num_of_results=2,
                                                estimated_result_length=100)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": summarize_text_2nd_grade_prompt}
    ],
    temperature=0.7
)

raw_output = response.choices[0].message.content

try:
    parsed = json.loads(raw_output)

    # Recalculate word count for each content
    for content in parsed["summary"]:
        item = content["content"]
        word_count = len(item.split())
        content["word_count"] = word_count

    print(json.dumps(parsed, indent=2))

except json.JSONDecodeError as e:
    print("Failed to parse JSON:", e)
    print("Raw response:", raw_output)

