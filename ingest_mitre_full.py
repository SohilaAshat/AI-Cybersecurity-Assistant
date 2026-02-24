import json
import chromadb

# Load MITRE Enterprise ATT&CK JSON
with open("enterprise-attack.json", "r", encoding="utf-8") as f:
    data = json.load(f)

client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="chroma_db",
        is_persistent=True
    )
)

# امسحي القديمة لو موجودة
try:
    client.delete_collection("cybersecurity_docs")
except:
    pass

collection = client.create_collection("cybersecurity_docs")

techniques = {}
mitigations = {}
relationships = []

# ===============================
# Parse MITRE objects
# ===============================
for obj in data["objects"]:

    # Techniques
    if obj.get("type") == "attack-pattern":
        ext_id = None
        for ref in obj.get("external_references", []):
            if ref.get("external_id"):
                ext_id = ref["external_id"]
                break

        if ext_id:
            techniques[obj["id"]] = {
                "external_id": ext_id,
                "name": obj.get("name", ""),
                "description": obj.get("description", "")
            }

    # Mitigations
    if obj.get("type") == "course-of-action":
        ext_id = None
        for ref in obj.get("external_references", []):
            if ref.get("external_id"):
                ext_id = ref["external_id"]
                break

        if ext_id:
            mitigations[obj["id"]] = {
                "external_id": ext_id,
                "name": obj.get("name", ""),
                "description": obj.get("description", "")
            }

    # Relationships
    if obj.get("type") == "relationship":
        if obj.get("relationship_type") == "mitigates":
            relationships.append(obj)

# ===============================
# Build final documents
# ===============================
documents = []
ids = []

for rel in relationships:
    source = rel["source_ref"]
    target = rel["target_ref"]

    if source in mitigations and target in techniques:

        mitigation = mitigations[source]
        technique = techniques[target]

        text = f"""
Technique {technique['external_id']}: {technique['name']}
Description: {technique['description']}

Mitigated by:
Mitigation {mitigation['external_id']}: {mitigation['name']}
Mitigation Description: {mitigation['description']}
"""

        documents.append(text.strip())
        ids.append(f"{technique['external_id']}_{mitigation['external_id']}")

collection.add(documents=documents, ids=ids)

print("Full MITRE ATT&CK with Mitigations ingested successfully!")
print(f"Total linked entries: {len(ids)}")