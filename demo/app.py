import sys
print(sys.path)

import streamlit as st
from llm_interface import ask_ollama
from inject import build_prompt

st.set_page_config(page_title="EU Grant Navigator (CAG + Ollama)")
st.title("🇪🇺 EU Grant Navigator (Local LLM)")

query = st.text_input("Ask your question about EU grants:")

if query:
    with st.spinner("Thinking..."):
        prompt = build_prompt(query, "src/data/processed_chunks/eu_grants_20250419-150436.json")
        response = ask_ollama(prompt)

    st.subheader("🧠 Answer")
    st.write(response)

    with st.expander("🔍 Show injected context"):
        st.code(prompt)
