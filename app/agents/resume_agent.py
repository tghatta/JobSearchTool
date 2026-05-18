from app.models.ollama_client import generate


class ResumeAgent:
    def tailor_resume(self, job_description: str):
        prompt = f"""
        Tailor my resume for this role.

        {job_description}
        """

        return generate(prompt)
