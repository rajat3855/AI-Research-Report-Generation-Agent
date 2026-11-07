from llm import get_llm
from search_tool import search_web
from reader import extract_text

llm = get_llm()

def research_topic(topic):

    queries = [
        f"{topic} overview",
        f"{topic} applications",
        f"{topic} advantages disadvantages",
        f"future of {topic}"
    ]

    knowledge = ""

    for q in queries:
        results = search_web(q)

        for r in results[:2]:
            text = extract_text(r["url"])
            knowledge += text + "\n\n"

    prompt = f"""
    Write a structured research report with:

    Introduction
    Working principle
    Applications
    Advantages
    Limitations
    Future scope

    DATA:
    {knowledge[:12000]}
    """

    report = llm.invoke(prompt)
    return report.content