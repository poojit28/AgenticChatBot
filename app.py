import streamlit as st

st.set_page_config(
    page_title="🤖 LANGGRAPH AGENTIC AI",
    layout="wide"
)

from src.langgraph_agentic_ai.main import app

if __name__=="__main__":
    app()