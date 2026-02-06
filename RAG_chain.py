from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from chromadb.config import Settings

from langchain_text_splitters import CharacterTextSplitter

from FAQ_chat_agent import OPENAI_API_KEY, BASE_URL

def get_doc():
    doc = TextLoader("./debug.txt").load()
    return CharacterTextSplitter(chunk_size = 500, chunk_overlap = 0).split_documents(doc)

def retriever(docs):
    embeddings = OpenAIEmbeddings(
        api_key=OPENAI_API_KEY,
        base_url=BASE_URL,
    )

    vectordb = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db", client_settings=Settings(anonymized_telemetry=False))
    return vectordb
