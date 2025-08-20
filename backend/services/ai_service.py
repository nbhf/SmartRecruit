from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def analyze_cv(text):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    prompt = f"""
    You are an information extractor.
    Extract the following fields from this CV and return ONLY valid JSON (no markdown, no explanation):
    {{
        "name": "...",
        "email": "...",
        "phone":"...",
        "education": ["..."],
        "skills": ["..."],
        "experience": ["..."]
    }}

    CV Text: {text}
    """
   
    response = llm.invoke(prompt)
    
    # Nettoyer la réponse pour s'assurer que c'est un JSON valide
    try:
        # Supprimer les éventuels markdown (```json)
        cleaned_response = response.content.replace('```json', '').replace('```', '').strip()
        json_data = json.loads(cleaned_response)
        return json_data  # Retourne directement le dict Python
    except json.JSONDecodeError as e:
        print(f"Erreur JSON: {e}")
        print(f"Réponse brute: {response.content}")
        return {"error": "Erreur d'analyse de la réponse AI"}