import streamlit as st
from llm import generate_response
from RAG_chain import get_doc, retriever 

st.set_page_config(page_title="Debug Agent", layout="wide")
st.title("Debug Agent")
st.markdown("Colle une erreur ou du code Python, l’IA te propose une correction.")

user_input = st.text_area("Colle ton code ou ton erreur ici", height=200)
if st.button("Analyser"):
    if not user_input.strip():
        st.warning("Veuillez entrer du code ou une erreur à analyser.")
    else:    
        with st.spinner("Analyse en cours..."):
            response = generate_response(retriever(get_doc()), user_input, get_doc())
            st.markdown(f"**Correction proposée :**\n\n{response}")
