import chromadb

client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="chroma_db",
        is_persistent=True
    )
)

collection = client.create_collection(name="cybersecurity_docs")

print("✅ Collection created successfully and saved.")