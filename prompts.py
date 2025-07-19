def generate_thesis(topic_description: str) -> str:
    prompt = f"""
You are an expert academic researcher and thesis writer. Your task is to write a complete, well-structured, 50-page thesis paper based on the following short topic description.

-------------------------
Topic Description:
"{topic_description}"
-------------------------

Thesis Requirements:
- The thesis must follow proper academic structure:
  1. Abstract (1 page)
  2. Introduction (3–4 pages)
  3. Literature Review (6–8 pages)
  4. Methodology (10–12 pages)
  5. Experimental Setup and Implementation (6–8 pages)
  6. Results and Evaluation (5–7 pages)
  7. Discussion (3–4 pages)
  8. Societal & Economic Impact (2–3 pages)
  9. Conclusion & Future Work (2–3 pages)
  10. References (3–5 pages)
  11. Appendices (5+ pages)
  
- Use formal academic tone and language
- Include relevant technical details, comparisons, and explanations
- Use dummy citations or real ones where necessary (APA style)
- Assume a publicly available dataset is used (e.g., from Kaggle)
- Include mention of tools like Python, TensorFlow/PyTorch
- Results should reflect realistic performance metrics (e.g., 95–99% accuracy)
- Include figures/tables placeholders where appropriate (e.g., [Figure 1: Sample fecal image])

Now, generate the full 50-page thesis accordingly.
"""
    return prompt


def summarize_text(text, num_of_results, estimated_result_length=2000):
    prompt = f"""
You are an expert AI text summarizer.

Summarize the following content by highlighting the key points, main arguments, and conclusion in a clear and structured manner.

Each summary should preserve the logic of the original text and be written in an academic, easy-to-understand style suitable for students.

------------------------------
Original Text:
\"\"\"{text}\"\"\"

Number of Summaries: {num_of_results}
Target Length per Summary: ~{estimated_result_length} words
------------------------------

Guidelines:
1. Extract all essential facts, ideas, and supporting arguments.
2. Maintain logical structure — if the original content is sectioned, follow that flow.
3. Avoid personal opinions, unnecessary repetition, or fluff.
4. Use clear and concise language that is informative and educational.
5. Each version must be unique in phrasing and structure.

Output Format:
Return your output as a valid JSON object with this structure:

{{
  "summaries": [
    {{
      "version": 1,
      "content": "Summary version 1 here (approx. {estimated_result_length} words)"
    }},
    // ... more if applicable
  ]
}}

Only return the JSON. Do not include markdown, commentary, or explanations.
"""
    return prompt


def pagewise_summarize_text(text):
    prompt = f"""
You are a highly skilled AI assistant specialized in reading and summarizing full PDF documents.

Your task is to summarize the following document **page by page**, returning the result as a **JSON object**.

Each page summary should include:
- `page`: the page number (integer)
- `title`: a short, meaningful title for this page (string)
- `details`: a clear and concise summary of the page’s content (string)

Guidelines:
- Do not include pages that are empty or contain no meaningful content.
- Do not repeat the same information across pages.
- Return the result as a **JSON array**, like this:

{{
  "summary": [
       {{
            "page": 1,
            "title": "Page Title Here",
            "details": "Summary of the page here..."
        }},
            ...
    ]
}}
      

Here is the document:
\"\"\"{text}\"\"\"

DO NOT include markdown backticks, commentary, or explanations. Only return valid JSON.
"""
    return prompt


def ai_code_generetor(programming_language, instructions):
    prompt = f"""
You are an expert AI coding assistant.

Write a complete, functional code in **{programming_language}** that performs the following task:

\"\"\"{instructions}\"\"\"

Include helpful comments for each step to explain the logic clearly.

------------------------------

Requirements:
1. Use clean, modular, and efficient code.
2. Add inline comments to explain each logical step clearly.
3. Use clear, meaningful variable and function names.
4. Follow the standard coding style for {programming_language}.
5. If helpful, include a sample input/output or test case.
6. Do NOT include any explanations outside of the code.
7. Assume any missing details if necessary — but stay focused on the core task.

Output Format:
Return your output as a valid JSON object in the following format:

{{
  "language": "{programming_language}",
  "code": "<full code with inline comments>"
}}

Only return the JSON object. Do NOT include markdown, commentary, or extra formatting.
"""
    return prompt


def content_rewrite(text, num_of_results, estimated_result_length):
    prompt = f"""
You are a professional content rewriting assistant.

Your task is to rewrite the following content into **{num_of_results} version(s)** that are clearer, more engaging, and professionally polished — without changing the original meaning.

------------------------------
**Original Content**:
\"\"\"{text}\"\"\"
------------------------------

**Rewrite Rules**:
1. Must write {num_of_results} version(s).
2. Keep the **original message and meaning fully intact**.
3. Improve grammar, flow, tone, and readability.
4. Make the text sound **natural, professional, and well-written**.
5. DO NOT add or remove ideas — just rewrite better.
6. Each version must be **exactly {estimated_result_length} words** — not more, not less.
7. Each version must be **unique** in style and phrasing.

Output Format:
Return the response as a **JSON object** in the following format:

{{
  "contents": [
    {{
      "version": "1",
      "content": "Rewritten version 1 here (exactly {estimated_result_length} words)"
    }},
    {{
      "version": "2",
      "content": "Rewritten version 2 here (exactly {estimated_result_length} words)"
    }}
    // ... repeat if more versions
  ]
}}

DO NOT include markdown backticks, commentary, or explanations. Only return valid JSON.
""" 
    return prompt

    
def article_generator_text(title, keywords=[], num_of_results=1, estimated_result_length=1000):
    keyword_str = ", ".join(keywords) if isinstance(keywords, list) else str(keywords)

    prompt = f"""
You are an expert AI content generator.

Generate {num_of_results} unique article version(s) based on the topic "{title}" and keywords "{keyword_str}".

Each article should be approximately {estimated_result_length} words long and include a strong introduction, structured body paragraphs, and a concise conclusion.

Write in a clear, engaging, and informative style suitable for SEO.

Return the results as a valid JSON object with this structure:

{{
  "articles": [
    {{
      "version": 1,
      "title": "{title}",
      "content": "Full article here (approx. {estimated_result_length} words)"
    }},
    // ... more if applicable
  ]
}}

Do NOT include markdown, explanations, or anything except the JSON.
"""
    return prompt


def paragraph_generator_text(paragraph_description, keywords=[], num_of_results=1, estimated_result_length=200):
    keyword_str = ", ".join(keywords) if isinstance(keywords, list) else str(keywords)

    prompt = f"""
You are an expert SEO content writer.

Your task is to generate **{num_of_results} completely unique paragraph(s)** based on the provided description and keywords. Each paragraph should be clear, informative, and suitable for digital content like blogs, articles, or educational material.

------------------------------
**Paragraph Description**: {paragraph_description}  
**Target Keywords**: {keyword_str}  
**Required Word Count per Paragraph**: Exactly {estimated_result_length} words  
**Total Paragraphs Required**: {num_of_results}
------------------------------

📌 Instructions:
1. Write exactly **{num_of_results}** unique paragraph(s).
2. Each paragraph must be **exactly {estimated_result_length} words** — not more, not less.
3. Each paragraph must be **semantically distinct** and must not reuse sentences or structure.
4. Naturally integrate the provided keywords into each paragraph without keyword stuffing.
5. Return your output as a **valid JSON object** in the following format:

{{
  "paragraphs": [
    {{
      "version": 1,
      "content": "First paragraph text here (escaped string, exactly {estimated_result_length} words)"
    }},
    {{
      "version": 2,
      "content": "Second paragraph text here"
    }}
    // ... more if applicable
  ]
}}

DO NOT include markdown backticks, commentary, or explanations. Only return valid JSON.
"""
    return prompt


def academic_essay_generator_text(title, keywords=[], num_of_results=1, estimated_result_length=2000):
    keyword_str = ", ".join(keywords) if isinstance(keywords, list) else str(keywords)

    prompt = f"""
You are a professional academic writer and researcher.

Your task is to write **{num_of_results} complete academic essay version(s)** based on the given title and keywords. Each essay must be **exactly {estimated_result_length} words** — not more, not less.

------------------------------
**Essay Title**: {title}  
**Target Keywords**: {keyword_str}  
**Exact Word Count per Essay**: {estimated_result_length} words  
**Number of Essay Versions Required**: {num_of_results}
------------------------------

Academic Essay Standards:
Each essay must strictly follow this structure:
1. Introduction (10–15% of total words)  
   - Clearly introduce the topic  
   - Present background/context  
   - End with a strong thesis statement

2. Body Paragraphs (70–80% of total words)  
   - Present arguments, supporting evidence, and examples  
   - Use clear topic sentences  
   - Ensure logical flow and coherence between paragraphs

3. Conclusion (10–15% of total words)  
   - Summarize main points  
   - Reinforce the thesis  
   - End with a closing thought or implication

Other Requirements:
- Use formal academic language and maintain a scholarly tone.
- Naturally integrate all keywords into each essay.
- Each version **must be exactly {estimated_result_length} words** — no more, no less.
- Do not include bullet points, subheadings, or any formatting.
- Do NOT include headings, markdown, word counts, or instructions.

Output Format:
Return your output as a **valid JSON object** structured as follows:

{{
  "essays": [
    {{
      "version": 1,
      "title": "{title}",
      "content": "Full essay text here, exactly {estimated_result_length} words"
    }},
    {{
      "version": 2,
      "title": "{title}",
      "content": "Second essay version here"
    }}
    // ... more if applicable
  ]
}}


Important:

Escape all newlines and double quotes properly (\\n, \\\").

Return only the raw JSON — no markdown backticks, no commentary or explanations.
"""
    return prompt
 
    
def summarize_text_2nd_grade(text, num_of_results, estimated_result_length=200):
    prompt = f"""
You are a friendly and smart helper who explains things so that a 2nd-grade student (about 7 years old) can easily understand.

 Your job is to read the text below and write **{num_of_results} simple summaries** for young kids.

------------------------------
 **Text to Summarize**:
\"\"\"{text}\"\"\"
------------------------------

 **Instructions**:
1. Use very **easy words** and **short, clear sentences**.
2. Write in a friendly, simple tone — like you're talking to a 7-year-old.
3. Do **not** add new ideas; only use what's in the original text.
4. Each summary must be **very close to {estimated_result_length} words** (within ±5%). Strictly avoid being too long or too short.
5. If multiple summaries are needed, make each one **different in wording** but covering the same main points.

 Output Format:
Return your output as a **valid JSON object** with this structure:

{{
  "summary": [
    {{
      "version": 1,
      "content": "Summary 1 text here (escaped string, approx {estimated_result_length} words)"
    }},
    {{
      "version": 2,
      "content": "Summary 2 text here"
    }}
    // ... more if applicable
  ]
}}

 Do NOT include any explanations, notes, or extra headings — just the summaries.
"""
    return prompt


# consider that extender means expanding the text
def text_extender(text, keywords=[], num_of_results=1, estimated_result_length=2000):
    keyword_str = ", ".join(keywords) if isinstance(keywords, list) else str(keywords)

    prompt = f"""
You are a professional writing assistant.

 Your task is to **expand and enrich** the given input text into **{num_of_results} longer, well-written version(s)**. Each version should preserve the original meaning while adding detail, clarity, and natural flow.

------------------------------
 **Original Text**:
\"\"\"{text}\"\"\"

 **Target Keywords (optional)**: {keyword_str}
 **Estimated Length per Version**: ~{estimated_result_length} words
 **Number of Versions Required**: {num_of_results}
------------------------------

 **Writing Guidelines**:
1. Keep the original intent and message of the text.
2. Add supporting details, background, examples, and context.
3. If keywords are provided, integrate them naturally into each version.
4. Use clear, engaging, grammatically correct language.
5. Maintain a consistent tone (formal, professional, or neutral unless the input suggests otherwise).
6. Each version must be approximately **{estimated_result_length} words** (±5%).
7. Each version must be unique in style and structure.

Output Format:
Return your output as a **valid JSON object** with the following structure:

{{
  "extended_texts": [
    {{
      "version": 1,
      "content": "Expanded version 1 text here (escaped, approx {estimated_result_length} words)"
    }},
    {{
      "version": 2,
      "content": "Expanded version 2 text here (escaped, approx {estimated_result_length} words)"
    }}
    // ... more if applicable
  ]
}}


 Do **not** include explanations, notes, or formatting — only return the expanded versions.
"""
    return prompt


def grammar_checker(text, num_of_results, estimated_result_length=2000):
    prompt = f"""
You are an expert grammar correction assistant.

Automatically correct all spelling, grammar, conjugation, and syntax errors in the following text while preserving the writing style and meaning.

------------------------------
Original Text:
\"\"\"{text}\"\"\"

Number of Corrected Versions Required: {num_of_results}
------------------------------

Correction Rules:
1. Correct all grammatical, spelling, and punctuation mistakes.
2. Preserve the original tone, wording, meaning, and structure unless changes are absolutely necessary for correctness.
3. If multiple versions are requested, ensure all versions follow the same principles.

Output Format:
Return your output as a valid JSON object structured as follows:

{{
  "corrections": [
    {{
      "version": 1,
      "content": "Corrected version 1 text here (escaped string)"
    }},
    {{
      "version": 2,
      "content": "Corrected version 2 text here"
    }}
    // ... more if applicable
  ]
}}

Do NOT include explanations, highlights, or comments — return only the clean corrected version(s).
"""
    return prompt


def dictionary(text, num_of_results, estimated_result_length=2000):
    prompt = f"""
You are a smart and detailed dictionary assistant.

 Your task is to provide a **full dictionary-style entry** for the given word or phrase: **"{text}"**

Include the following details for each version (if multiple requested):

------------------------------
 **Word or Phrase**: {text}
 **Number of Definitions Required**: {num_of_results}
 **Estimated Length per Entry**: ~{estimated_result_length} characters
------------------------------

 **Entry Format for Each Version**:
- **Word**: {text}
- **Part of Speech**: (e.g., noun, verb, adjective)
- **Pronunciation**: (in IPA or plain English if available)
- **Definition**: Clear and accurate meaning
- **Example Sentence**: Use the word in a natural sentence
- **Synonyms**: List 3–5 related words
- **Antonyms** (if applicable): Optional
- **Origin/Etymology**: Briefly mention origin if known

Output Format:
Return your output as a **valid JSON object** with this structure:

{{
  "dictionary_entries": [
    {{
      "version": 1,
      "word": "{text}",
      "part_of_speech": "noun",
      "pronunciation": "/ˈwɜrd/",
      "definition": "Clear and accurate meaning here.",
      "example_sentence": "This is an example sentence using the word.",
      "synonyms": ["term", "expression", "locution"],
      "antonyms": ["silence"],
      "origin": "From Old English ..."
    }},
    {{
      "version": 2,
      "word": "{text}",
      "part_of_speech": "verb",
      "pronunciation": "/wɜrd/",
      "definition": "Another meaning here.",
      "example_sentence": "Example sentence here.",
      "synonyms": ["say", "state", "express"],
      "antonyms": [],
      "origin": "Origin details..."
    }}
    // ... more if applicable
  ]
}}

 Do NOT add commentary, formatting instructions, or unrelated content. Just return the dictionary entries.
"""
    return prompt


def exercise_corrector_prompt(text, num_of_results, estimated_result_length=2000):
    prompt = f"""
You are an expert AI assistant that reviews and corrects student responses to exercises, including multiple-choice, calculations, essays, and short answers.

Your task is to:
- Provide a corrected version of the student's response.
- Explain all corrections **thoroughly and step by step** using clear, precise pedagogical reasoning.

------------------------------
Student Response:
\"\"\"{text}\"\"\"

Number of Corrected Versions Required: {num_of_results}
Estimated Length per Version: ~{estimated_result_length} words
------------------------------

Correction Guidelines:
1. Correct all types of errors: grammar, spelling, punctuation, structure, logic, factual mistakes, and misconceptions.
2. For each version, include a "corrected_text" (the revised student response).
3. Then include a "steps" list:
   - Each step must explain:
     - What was incorrect.
     - What it was changed to.
     - Why the correction was necessary — with pedagogical justification (explain the rule or logic clearly, like teaching the student).
4. Do not change the original intent of the response unless factual accuracy requires it.
5. Ensure each version is phrased slightly differently while delivering the same core corrections.
6. Use a supportive, clear, and teacher-like tone focused on helping the student learn.

Output Format:
Return your output as a valid JSON object with this exact structure:

{{
  "corrections": [
    {{
      "version": 1,
      "corrected_text": "Fully corrected version here.",
      "steps": [
        {{
          "original": "Original text fragment.",
          "correction": "Corrected version.",
          "explanation": "Pedagogical reasoning for this change."
        }},
        ...
      ]
    }},
    {{
      "version": 2,
      "corrected_text": "Alternative corrected version.",
      "steps": [
        ...
      ]
    }}
  ]
}}

Rules:
- Do NOT include any extra comments, markdown formatting, or instructions.
- ONLY return the JSON object in the specified structure.
"""
    return prompt


def assist_student_chatbot_prompt():
    prompt = f"""
You are a helpful and friendly AI tutor.
You assist students by answering questions clearly, step-by-step, and in simple language.
Always explain any reasoning or logic if the question involves problem-solving or analysis.
Be polite, concise, and educational.
"""
    return prompt


def humanizer_prompt(text, intensity_level="medium", literacy_level="high school"):
    prompt = f"""
You are a skilled and helpful AI writing assistant trained to make technical or robotic text sound more natural, conversational, and human.

Your task is to **rewrite the following text** based on the user's preferences:

------------------------------
**Original Text**:
{text}
------------------------------

**Humanization Guidelines**:
1. Use a **{intensity_level} level of humanization**, where:
   - Low = slight polishing, still formal
   - Medium = friendly, semi-formal
   - High = highly conversational, expressive, natural
2. Adapt the tone and vocabulary to match a **{literacy_level} reading level**.
3. Keep the original meaning intact — do **not** add or remove factual content.
4. Improve grammar, sentence flow, and clarity where needed.
5. Be helpful, easy to understand, and appropriate for the specified audience.

Output Format:  
Return your output as a **valid JSON object** with the following structure:

{{
  "humanized_text": "<rewritten version here (escaped)>"
}}

Only return the rewritten version. Do not include formatting instructions or meta-comments.
"""
    return prompt



# not sure if this is needed, but keeping it for now
def topic_generator_text(text,topic,max_length_of_topic, language, writing_tone, creativity,point_of_view,article_length):
    prompt = f"""
You are a highly skilled AI assistant specialized in reading and summarizing full PDF documents.

Your task is to summarize the following document **page by page**, using the structure below:

------------------------------
 Page X:
**Title**: <short, meaningful title for this page>  
**Details**: <clear and concise summary of this page’s content>
------------------------------

 Guidelines:
- Always start each page with "Page X" (e.g., Page 1, Page 2).
- Generate a relevant **title** for each page, based on the page’s topic.
- Write a **brief but informative summary** under **Details**.
- Assume the content is already structured by page and analyze it accordingly.
- Skip any pages that are empty or have no meaningful content.
- Do **not repeat** the same information across pages.

 Document:
\"\"\"{text}\"\"\"

 Generate the full summary in the required format:
"""
    return prompt
