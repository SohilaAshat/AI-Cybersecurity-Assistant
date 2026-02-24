import json
from langchain.text_splitter import CharacterTextSplitter
from chromadb.utils import embedding_functions
import chromadb

# Load MITRE ATT&CK JSON
with open("enterprise-attack.json", "r", encoding="utf-8") as f:
    attack_data = json.load(f)

# Extract techniques
techniques = []
for obj in attack_data.get("objects", []):
    if obj.get("type") == "attack-pattern":
        tid = obj.get("external_references", [{}])[0].get("external_id")
        name = obj.get("name")
        desc = obj.get("description", "")
        if tid and desc:
            techniques.append({
                "id": tid,
                "name": name,
                "description": desc
            })

# Split long descriptions into chunks
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=500,
    chunk_overlap=50
)

documents = []
metadatas = []
for tech in techniques:
    chunks = splitter.split_text(tech["description"])
    for c in chunks:
        documents.append(c)
        metadatas.append({
            "technique_id": tech["id"],
            "technique_name": tech["name"]
        })

# Initialize Chroma client
client = chromadb.Client()
collection_name = "cybersecurity_docs"

# Delete existing collection if exists
try:
    client.delete_collection(collection_name)
except:
    pass

collection = client.create_collection(name=collection_name)

# Use OpenAI embeddings (replace with your embedding function)
emb_func = embedding_functions.OpenAIEmbeddingFunction(api_key="YOUR_OPENAI_KEY", model_name="text-embedding-3-large")

# Add documents to collection
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=[f"doc_{i}" for i in range(len(documents))],
    embedding_function=emb_func
)

print(f"✅ Vector DB built with {len(documents)} chunks")