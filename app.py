# Streamlit App mit LlamaIndex + OpenAI
import streamlit as st
from llama_index.core import StorageContext, load_index_from_storage


st.set_page_config(page_title="Helvetia GPT", layout="wide")
st.title('Helvetia GPT')

# Index laden
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Frageingabe
query = st.text_input('Frage zur Versicherung:')

if query:
    # Anfrage an den Index
    query_engine = index.as_query_engine()
    response = query_engine.query(query)

    # Ausgabe
    st.write(response)
