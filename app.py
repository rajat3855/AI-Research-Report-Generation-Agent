import streamlit as st
from agent import research_topic
from report import save_markdown

st.title("AI Research Agent")

topic = st.text_input("Enter Research Topic")

if st.button("Generate Report"):
    with st.spinner("Researching..."):
        report = research_topic(topic)
        file = save_markdown(topic, report)

        st.success("Report Generated!")
        st.write(report)