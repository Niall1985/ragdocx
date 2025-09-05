import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('gemini_api')
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

def llm(query, context):
    prompt = f"""You are an agent whose job is to take the query and context and based on the query, structure the context and return an answer: +
    Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"""

    response = model.generate_content(prompt)
    return response.text
