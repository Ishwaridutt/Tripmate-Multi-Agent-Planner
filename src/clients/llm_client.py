from config.config import GROQ_API_KEY, GROQ_MODEL_NAME
from langchain_groq import ChatGroq

llm_client = ChatGroq(
    model=GROQ_MODEL_NAME,
    api_key=GROQ_API_KEY
)

