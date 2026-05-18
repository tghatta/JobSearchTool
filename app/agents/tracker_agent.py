from app.database.db import SessionLocal
from app.database.models import Job


class TrackerAgent:
    def save_job(self, job_data):
        db = SessionLocal()

        job = Job(
            title=job_data.get("title"),
            company=job_data.get("company"),
            location=job_data.get("location"),
            url=job_data.get("url"),
            score=job_data.get("score", 0),
            status="NEW"
        )

        db.add(job)
        db.commit()
        db.close()
