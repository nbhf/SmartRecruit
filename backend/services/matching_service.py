from models.cv import CV
from models.job import JobOffer, db
from langchain_google_genai import ChatGoogleGenerativeAI
import json

from models.job import db
from models.match import CVJobMatch

def save_cv_job_matches(matches, job_id):
    for match in matches:
            new_match = CVJobMatch(
                cv_id=match["cv_id"],
                job_id=job_id,
                score=match["score"],
                skills_match=match["skills_match"],
                experience_match=match["experience_match"],
                education_match=match["education_match"],
                justification=match["justification"]
            )
            db.session.add(new_match)
    db.session.commit()


# Initialise le LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def score_cv_for_job(cv: CV, job: JobOffer):
    # Prépare les JSON pour le prompt
    cv_json = json.dumps({
        "name": cv.name,
        "email": cv.email,
        "phone": cv.phone,
        "education": cv.education,
        "skills": cv.skills,
        "experience": cv.experience
    })

    job_json = json.dumps({
        "title": job.title,
        "skills_required": job.description,  # ou liste de skills si séparée
        "location": job.location,
        "salary": job.salary
    })

    prompt = f"""
You are an expert recruiter.
Evaluate how well this candidate fits the following job offer.

Job Offer:
{job_json}

Candidate CV:
{cv_json}

Scoring Criteria (total 100 points):
- Skills match: 50 points
- Experience match: 30 points
- Education match: 20 points

Return ONLY  valid JSON objects:
Return ONLY valid JSON like this:
{{
  "Candidate name": "...",
  "score": 78,
  "skills_match": 40,
  "experience_match": 25,
  "education_match": 13,
  "justification": "..."
}}

 All numeric fields MUST be integers between 0 and their maximum (score: 0–100, skills_match: 0–50, experience_match: 0–30, education_match: 0–20). 
Do not return strings or fractions like '25/100'.

Do not include markdown, backticks or this ```json

"""

    response = llm.invoke(prompt)
    print("RAW LLM RESPONSE:", response.content)
    try:
         # Supprimer les éventuels markdown (```json)
        cleaned_response = response.content.replace('```json', '').replace('```', '').strip()
        result = json.loads(cleaned_response )
        return result
    except Exception as e:
        print("Error parsing LLM response:", e)
        return None



def match_all_cvs_to_job(job_id: int):
    job = JobOffer.query.get(job_id)
    if not job:
        return []

    cvs = CV.query.all()
    matches = []

    for cv in cvs:
        # Vérifie si ce CV est déjà matché avec ce job
        existing_match = CVJobMatch.query.filter_by(cv_id=cv.id, job_id=job_id).first()
        
        if existing_match:
            # Ajoute le match existant sans refaire le scoring
            matches.append({
                "cv_id": cv.id,
                "cv_name": cv.name,
                "score": existing_match.score,
                "skills_match": existing_match.skills_match,
                "experience_match": existing_match.experience_match,
                "education_match": existing_match.education_match,
                "justification": existing_match.justification
            })
        else:
            # Si pas encore matché → calcul via LLM
            score_data = score_cv_for_job(cv, job)
            if score_data:
                new_match = {
                    "cv_id": cv.id,
                    "cv_name": cv.name,
                    "score": score_data.get("score"),
                    "skills_match": score_data.get("skills_match"),
                    "experience_match": score_data.get("experience_match"),
                    "education_match": score_data.get("education_match"),
                    "justification": score_data.get("justification")
                }
                matches.append(new_match)

                # Sauvegarde direct en DB pour éviter double traitement
                save_cv_job_matches([new_match], job_id)

    # Tri décroissant par score
    matches.sort(key=lambda x: x["score"], reverse=True)

    return matches


