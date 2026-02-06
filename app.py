import streamlit as st

import FAQ_chat_agent

st.set_page_config(page_title="Debug Agent", layout="wide")
st.title("Debug Agent")
st.markdown("Colle une erreur ou du code Python, l’IA te propose une correction.")

user_input = st.text_area("Colle ton code ou ton erreur ici", height=200)
if st.button("Analyser"):
    if not user_input.strip():
        st.warning("Veuillez entrer du code ou une erreur à analyser.")
    else:    
        with st.spinner("Analyse en cours..."):
            response = FAQ_chat_agent.generate_response(FAQ_chat_agent.retriever(FAQ_chat_agent.get_doc()), user_input, FAQ_chat_agent.get_doc())
            st.markdown(f"**Correction proposée :**\n\n{response}")
