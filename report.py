def save_markdown(topic, content):
    filename = topic.replace(" ", "_") + ".md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n")
        f.write(content)
    return filename