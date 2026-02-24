import chromadb

client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="chroma_db",
        is_persistent=True
    )
)

client.delete_collection("cybersecurity_docs")
print("Old collection deleted.")