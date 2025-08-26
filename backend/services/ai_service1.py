from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def analyze_cv(filepath):
    # 1️⃣ Charger le PDF
    loader = PyPDFLoader(filepath)
    documents = loader.load()  # liste de pages

    # 2️⃣ Préparer le prompt pour extraire les infos importantes
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
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
    )

    # 3️⃣ Créer la chaîne LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    chain = LLMChain(llm=llm, prompt=prompt)

    # 4️⃣ Exécuter la chaîne page par page
    extracted_info = {
        "name": None,
        "email": None,
        "phone": None,
        "education": [],
        "skills": [],
        "experience": []
    }

    for doc in documents:
        full_text = " ".join([doc.page_content for doc in documents])
        response = chain.run(full_text)

        try:
            cleaned_response = response.replace('```json', '').replace('```', '').strip()
            data = json.loads(cleaned_response)
            # Fusionner les résultats page par page
            for key in extracted_info:
                if isinstance(extracted_info[key], list):
                    extracted_info[key].extend(data.get(key, []))
                else:
                    if not extracted_info[key]:
                        extracted_info[key] = data.get(key)
            print(extracted_info)
            return extracted_info
        except Exception as e:
            print("Erreur parsing JSON:", e)
            print("Réponse brute du modèle:", response )
            return {"error": "Erreur d'analyse de la réponse AI"}

    # 5️⃣ Afficher le résultat final
    print(json.dumps(extracted_info, indent=2, ensure_ascii=False))
