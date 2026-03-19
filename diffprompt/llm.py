import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_prompt(prompt: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Send a prompt to the LLM and return the response as a string."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0  # keep outputs deterministic for fair comparison
    )
    return response.choices[0].message.content.strip()