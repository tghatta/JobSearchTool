from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
DATABASE_URL = os.getenv("DATABASE_URL")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
MAX_APPLICATIONS_PER_DAY = int(
    os.getenv("MAX_APPLICATIONS_PER_DAY", 20)
)
