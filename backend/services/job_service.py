from models.job import db, JobOffer

def create_job_offer(data):
    job = JobOffer(
        title=data.get("title"),
        company=data.get("company"),
        description=data.get("description"),
        location=data.get("location"),
        salary=data.get("salary") 
    )
    db.session.add(job)
    db.session.commit()
    return job
