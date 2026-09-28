import os
from dotenv import load_dotenv
load_dotenv()


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
DEFAULT_ORIGIN_IATA = os.getenv("DEFAULT_ORIGIN_DATA")
AVIATION_BASE_URL = "https://api.aviationstack.com/v1/flights"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL_NAME = "openai/gpt-oss-120b"
SQLITE_DATABASE_PATH = "tripmate_agent.db"


if not SQLITE_DATABASE_PATH:
    raise ValueError(
        "\nSQLITE_DATABASE_PATH is missing. Please add your SQLITE DB Path to your config"
    )

if not GROQ_API_KEY:
    raise ValueError("\nGROQ_API_KEY is missing. Please add it to your .env file.")





