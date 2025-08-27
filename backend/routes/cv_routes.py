from flask import Blueprint, request, jsonify
from services.ai_service import analyze_cv
import os
from models.cv import  CV 
from models.job import db

cv_bp = Blueprint("cv_bp", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@cv_bp.route("/cvUpload", methods=["POST"])
def upload_cv():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    # Analyse avec AI
    analysis_data = analyze_cv(filepath) 
    
    if "error" in analysis_data:
        return jsonify({"error": analysis_data["error"]}), 500
    
    try:
        # Créer un nouveau CV dans la base de données
        new_cv = CV(
            name=analysis_data.get("name", ""),
            email=analysis_data.get("email", ""),
            phone=analysis_data.get("phone", ""),
            education=analysis_data.get("education", []),
            skills=analysis_data.get("skills", []),
            experience=analysis_data.get("experience", []),
            file_path=filepath
        )
        
        db.session.add(new_cv)
        db.session.commit()
        
        return jsonify({
            "message": "CV analysé et enregistré avec succès",
            "cv_id": new_cv.id,
            "analysis": analysis_data  
        })
        
    except Exception as e:
        db.session.rollback()
        print(f"Erreur de base de données: {str(e)}")
        return jsonify({"error": f"Erreur de base de données: {str(e)}"}), 500
    

@cv_bp.route("/cvUpload/all", methods=["GET"])
def get_all_cvs():
    cvs = CV.query.order_by(CV.uploaded_at.desc()).all()
    result = [ { "id": cv.id, "name": cv.name, "skills": cv.skills, "experience": cv.experience } for cv in cvs ]
    return jsonify(result)
