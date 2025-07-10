# index_builder.py

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

def build_index():
    pdf_dir = "data"
    storage_dir = "storage"

    if not os.path.exists(pdf_dir):
        print(f"Ordner '{pdf_dir}' nicht gefunden!")
        return

    # Lade alle PDFs aus dem data-Ordner
    documents = SimpleDirectoryReader(pdf_dir).load_data()

    # Index erzeugen
    index = VectorStoreIndex.from_documents(documents)

    # Speichern
    index.storage_context.persist(persist_dir=storage_dir)
    print("✅ Index wurde erfolgreich erstellt und gespeichert!")

if __name__ == "__main__":
    build_index()
