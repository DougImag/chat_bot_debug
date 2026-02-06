import os
from dotenv import load_dotenv

from openai import OpenAI

from langchain_core.prompts.chat import SystemMessagePromptTemplate

from colorama import Fore

load_dotenv()
 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGUAGE_MODEL = "openai/gpt-oss-20b:free"
BASE_URL = "https://openrouter.ai/api/v1"

MODEL = OpenAI(
    base_url = BASE_URL,
    api_key = OPENAI_API_KEY,
)

ROLE = """Vous etes un expert Python specialise dans le debogage. Votre mission :
                - Analyser le code fourni par l utilisateur
                - Identifier l erreur ou le bug potentiel
                - Expliquer clairement la cause
                - Proposer une correction concrete avec du code
        Basez-vous uniquement sur le contexte fourni.
        Si l information est insuffisante, demandez le traceback ou le code complet. """

system_message_prompt = SystemMessagePromptTemplate.from_template(ROLE)
