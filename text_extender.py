from dotenv import load_dotenv
# from groq import Groq
# import json
import os
# import re
# from groq import Groq
from prompts import text_extender
from openai import OpenAI


load_dotenv()

# text extender prompt
text_extender_prompt = text_extender(text="Artificial intelligence is changing the way we work and live.",
                                            keywords=["AI", "automation", "technology"],
                                            num_of_results=2,
                                            estimated_result_length=300)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": text_extender_prompt
      }
    ],
    temperature=0.7,
)
    
print(response.choices[0].message.content)

