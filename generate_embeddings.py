import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()

collection = client.get_or_create_collection(name="cybersecurity_docs")

documents = [
    "Phishing is a common attack to gain initial access.",
    "MITRE ATT&CK T1566 explains phishing techniques.",
    "Spear phishing targets specific individuals.",
    "Whaling is a phishing attack against executives.",
    "Ransomware encrypts victim files to demand ransom.",
    "MITRE ATT&CK T1486 describes ransomware behavior.",
    "StackExchange Q&A about network security best practices.",
    "Security guides: How to implement multi-factor authentication (MFA)."
]

metadatas = [
    {"source": "MITRE ATT&CK", "type": "technique"},
    {"source": "MITRE ATT&CK", "type": "technique"},
    {"source": "MITRE ATT&CK", "type": "technique"},
    {"source": "MITRE ATT&CK", "type": "technique"},
    {"source": "MITRE ATT&CK", "type": "malware"},
    {"source": "MITRE ATT&CK", "type": "malware"},
    {"source": "StackExchange", "type": "Q&A"},
    {"source": "Security Guide", "type": "defense"}
]

embedding_fn = embedding_functions.ChromaBm25EmbeddingFunction()

if len(collection.get()) == 0:
    collection.add(
        ids=[f"doc{i}" for i in range(len(documents))],
        documents=documents,
        metadatas=metadatas,
        embedding_function=embedding_fn
    )
    print("✅ Documents added to ChromaDB!")
else:
    print("⚠️ Collection already has documents. Skipping add.")