import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL"),
    temperature=0
)

def ask_ai(prompt):

    system_prompt = f"""
You are an expert AI Research Assistant.

Rules:
- Answer ONLY using the provided context.
- Never invent facts.
- Never expand abbreviations unless they appear in the context.
- If the answer is not available, reply:
'I could not find this information in the uploaded research paper.'
- Keep answers concise and professional.

{prompt}
"""

    response = llm.invoke(system_prompt)
    return response.content