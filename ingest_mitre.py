import json
import chromadb

# Load MITRE JSON
with open("enterprise-attack.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Connect to Chroma
client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="chroma_db",
        is_persistent=True
    )
)

collection = client.create_collection("cybersecurity_docs")

documents = []
ids = []

for obj in data["objects"]:
    if obj.get("type") == "attack-pattern":
        name = obj.get("name", "")
        description = obj.get("description", "")

        # Get technique ID
        technique_id = None
        for ref in obj.get("external_references", []):
            if ref.get("external_id"):
                technique_id = ref.get("external_id")
                break

        if technique_id and description:
            text = f"Technique {technique_id}: {name}. Description: {description}"
            documents.append(text)
            ids.append(technique_id)

collection.add(
    documents=documents,
    ids=ids
)

print("MITRE ATT&CK ingested successfully!")
print(f"Total techniques added: {len(ids)}")