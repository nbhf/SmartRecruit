from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models.job import db

class CVJobMatch(db.Model):
    __tablename__ = "cv_job_matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cv_id = db.Column(db.Integer, db.ForeignKey("Cv_analysis.id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job_offers.id"), nullable=False)
    score = db.Column(db.Float)
    skills_match = db.Column(db.Float)
    experience_match = db.Column(db.Float)
    education_match = db.Column(db.Float)
    justification = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations optionnelles pour facilité de jointure
    cv = db.relationship("CV", backref="job_matches")
    job = db.relationship("JobOffer", backref="cv_matches")
