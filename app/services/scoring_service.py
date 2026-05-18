from app.models.ollama_client import generate


def score_job(description: str):
    prompt = f"""
    Decide whether this is a good match.

    {description}
    """

    return generate(prompt)
