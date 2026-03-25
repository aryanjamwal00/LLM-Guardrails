import streamlit as st
from classifier import classify_prompt

st.title("🛡️ LLM Guardrails Firewall")

prompt = st.text_area("Enter your prompt:")

if st.button("Check"):
    safe, category, confidence = classify_prompt(prompt)

    st.write("### Result:")
    st.write(f"Safe: {safe}")
    st.write(f"Category: {category}")
    st.write(f"Confidence: {confidence}")