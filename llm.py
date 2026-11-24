from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)



def get_llm():
    return ChatOllama(
        model="llama3",
        temperature=0.2
    )