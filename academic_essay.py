from dotenv import load_dotenv
# from groq import Groq
# import json
import os
# import re
# from groq import Groq
from prompts import academic_essay_generator_text
from openai import OpenAI


load_dotenv()

# academic essay generator prompt
academic_essay_generator_prompt = academic_essay_generator_text(title="The Role of Renewable Energy in Combating Climate Change",
                                                keywords=["renewable energy", "carbon emissions", "climate change"],
                                                num_of_results=2,
                                                estimated_result_length=150)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": academic_essay_generator_prompt
      }
    ],
    temperature=0.7,
)
    
print(response.choices[0].message.content)

