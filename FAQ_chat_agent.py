import os
from dotenv import load_dotenv

from openai import OpenAI

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts.chat import SystemMessagePromptTemplate

from colorama import Fore

load_dotenv()
 
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGUAGE_MODEL = "openai/gpt-oss-20b:free"
BASE_URL = "https://openrouter.ai/api/v1"

model = OpenAI(
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

response = model.chat.completions.create(
        model=LANGUAGE_MODEL,
        messages=[
                {
                    "role": "user",
                    "content": ROLE
                }
                ],
        extra_body={"reasoning": {"enabled": True}}
)

system_message_prompt = SystemMessagePromptTemplate.from_template(ROLE)

def get_doc():
    doc = TextLoader("./debug.txt").load()
    return CharacterTextSplitter(chunk_size = 500, chunk_overlap = 0).split_documents(doc)

def retriever(docs):
    embeddings = OpenAIEmbeddings(
        api_key=OPENAI_API_KEY,
        base_url=BASE_URL,
    )

    vectordb = Chroma.from_documents(docs, embeddings)
    return vectordb

def generate_response(retriev, user_input, docs):
    retriev.similarity_search(user_input)
    context = "\n\n".join(d.page_content for d in docs)
    response = model.chat.completions.create(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "system", "content": ROLE},
            {"role": "user", "content": f"CONTEXTE:\n{context}\n\nQUESTION:\n{user_input}"}
        ]
    )
    return response.choices[0].message.content


def boucle():
    documents = get_doc()
    retriev = retriever(documents)
    while True:
        user_input = input("\nAs tu une question?\n\n")
        if user_input == "x":
            break
        reponse = generate_response(retriev, user_input, documents)
        print(f"\n {reponse}")


if __name__ == "__main__":
    boucle()
