from flask import Flask
from routes.cv_routes import cv_bp
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from routes.job_routes import job_bp
from models.job import db


app = Flask(__name__)
CORS(app)  # autorise le frontend React à appeler Flask


# Configuration PostgreSQL locale
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@localhost:5432/SmartRecruit"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()



# Register Blueprints
app.register_blueprint(cv_bp, url_prefix="/api")
app.register_blueprint(job_bp, url_prefix="/api")




if __name__ == "__main__":
    app.run(debug=True)
