from flask import Blueprint, request, jsonify
from services.job_service import create_job_offer
from models.job import JobOffer
from services.matching_service import match_all_cvs_to_job


job_bp = Blueprint("job_bp", __name__)

@job_bp.route("/jobs", methods=["POST"])
def add_job():
    try:
        data = request.json
        print("========== Received job data ==========", data)
        job = create_job_offer(data)
        return jsonify({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "description": job.description,
            "location": job.location,
            "salary": job.salary,
            "created_at": job.created_at
        }), 201
    except Exception as e:
        print("ERROR in /jobs:", str(e))
        return jsonify({"error": str(e)}), 400


@job_bp.route("/jobs/all", methods=["GET"])
def get_all_jobs():
    jobs = JobOffer.query.order_by(JobOffer.created_at.desc()).all()
    result = [ { "id": job.id, "title": job.title, "company": job.company } for job in jobs ]
    return jsonify(result)


@job_bp.route("/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    job = JobOffer.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    return jsonify({
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "description": job.description,
        "location": job.location,
        "salary": job.salary,
        "created_at": job.created_at
    })

@job_bp.route("/jobs/<int:job_id>/match", methods=["GET"])
def match_job(job_id):
    try:
        matches = match_all_cvs_to_job(job_id)
        return jsonify(matches), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

from models.job import JobOffer, db

@job_bp.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    job = JobOffer.query.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted"}), 200


@job_bp.route('/jobs/bulk', methods=['POST'])
def add_jobs_bulk():
    jobs = request.json  # attendu: une liste de jobs
    added_jobs = []
    for job_data in jobs:
        job = JobOffer(
            title=job_data['title'],
            description=job_data['description'],
            company=job_data['company'],
            location=job_data['location'],
            salary=job_data.get('salary')
        )
        db.session.add(job)
        added_jobs.append(job_data)
    db.session.commit()
    return jsonify({"added": added_jobs}), 201