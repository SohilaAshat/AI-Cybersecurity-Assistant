import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection(name="cybersecurity_docs")

new_documents = [
    "Zero-day vulnerabilities allow attackers to exploit unknown bugs.",
    "Social engineering attacks trick users into giving credentials."
]

new_metadatas = [
    {"source": "CVE Database", "type": "vulnerability"},
    {"source": "Security Guide", "type": "technique"}
]

collection.add(
    ids=[f"doc_new{i}" for i in range(len(new_documents))],
    documents=new_documents,
    metadatas=new_metadatas
)

print("✅ New documents added!")