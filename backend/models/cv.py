from datetime import datetime
from models.job import db

class CV(db.Model):
    __tablename__ = "Cv_analysis"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    education = db.Column(db.JSON)  
    skills = db.Column(db.JSON)
    experience = db.Column(db.JSON)
    file_path = db.Column(db.String(200))
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())