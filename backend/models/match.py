from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models.job import db

class CVJobMatch(db.Model):
    __tablename__ = "cv_job_matches"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cv_id = db.Column(db.Integer, db.ForeignKey("Cv_analysis.id", ondelete="CASCADE"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job_offers.id", ondelete="CASCADE"), nullable=False)
    score = db.Column(db.Float)
    skills_match = db.Column(db.Float)
    experience_match = db.Column(db.Float)
    education_match = db.Column(db.Float)
    justification = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relations optionnelles pour facilité de jointure
    cv = db.relationship("CV",  backref=db.backref("job_matches", cascade="all, delete-orphan"))
    job = db.relationship("JobOffer", backref=db.backref("job_matches", cascade="all, delete-orphan"))
