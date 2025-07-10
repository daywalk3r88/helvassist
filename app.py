# Streamlit App

import streamlit as st

st.title('Helvetia GPT')

query = st.text_input('Frage zur Versicherung:')
if query:
    st.write('Antwort kommt hier hin...')