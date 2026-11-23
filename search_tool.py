import os
from tavily import TavilyClient
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY not found. Check .env file location.")

client = TavilyClient(api_key=api_key)

def search_web(query):
    results = client.search(query=query, search_depth="advanced", max_results=5)
    return results["results"]