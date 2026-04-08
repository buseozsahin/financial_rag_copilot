import requests
from rag_config import get_rag_config

OLLAMA_URL = "http://localhost:11434/api/generate"


def build_prompt(query, chunks, style):
    context = "\n\n".join(chunks)

    return f"""
    You are a STRICT financial QA system.
    
    STYLE: {style}
    
    CRITICAL RULES:
    1. Use ONLY the information inside the provided chunks.
    2. You are NOT allowed to use any outside knowledge.
    3. If the answer is not explicitly in the chunks, respond EXACTLY:
       "I don't have enough information in the provided chunks."
    4. Do NOT guess. Do NOT infer. Do NOT assume.
    
    ---
    
    CONTEXT:
    {context}
    
    ---
    
    QUESTION:
    {query}
    
    ---
    INSTRUCTIONS:
    - Always structure the answer in "Pros and Cons" format
    - Be concise and financial-analysis focused
    - Do not add information not supported by context
    
    Format:
    
    PROS:
    - ...
    
    CONS:
    - ...
    
    ---
    
    ANSWER:
    """

def call_llm(prompt, tokens):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": tokens
            }
        }
    )
    return response.json()

def get_llm_answer(query, chunks, mode):
    config = get_rag_config(mode)
    style = config["style"]
    tokens = config["max_tokens"]

    prompt = build_prompt(query, chunks, style)
    result = call_llm(prompt, tokens)

    return result
