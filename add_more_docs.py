import chromadb
from chromadb.utils import embedding_functions
import numpy as np

client = chromadb.Client()
collection = client.get_or_create_collection(name="cybersecurity_docs")

new_documents = [
    "Phishing emails often use urgent language to trick victims.",
    "SQL Injection allows attackers to manipulate database queries.",
    "Cross-Site Scripting (XSS) injects malicious scripts into web pages.",
    "Multi-factor authentication (MFA) adds an extra layer of security.",
    "Ransomware attacks encrypt files and demand payment.",
]

new_metadatas = [
    {"source": "Security Guide", "type": "technique"},
    {"source": "Security Guide", "type": "vulnerability"},
    {"source": "Security Guide", "type": "vulnerability"},
    {"source": "Security Guide", "type": "defense"},
    {"source": "Security Guide", "type": "malware"},
]

embedding_fn = embedding_functions.ChromaBm25EmbeddingFunction()

sparse_embeddings = embedding_fn(new_documents)

embeddings_list = []
for se in sparse_embeddings:
    arr = np.zeros(max(se.indices)+1, dtype=float)
    for idx, val in zip(se.indices, se.values):
        arr[idx] = val
    embeddings_list.append(arr.tolist())

collection.add(
    ids=[f"doc_new{i}" for i in range(len(new_documents))],
    documents=new_documents,
    metadatas=new_metadatas,
    embeddings=embeddings_list
)

print("✅ New documents added successfully!")