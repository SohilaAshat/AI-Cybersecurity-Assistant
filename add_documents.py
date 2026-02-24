import chromadb

client = chromadb.Client(
    settings=chromadb.config.Settings(
        persist_directory="chroma_db",
        is_persistent=True
    )
)

collection = client.get_collection("cybersecurity_docs")

documents = [
    "SQL Injection is a web security vulnerability that allows attackers to interfere with database queries.",
    "Phishing is a social engineering attack used to steal user data including login credentials.",
    "Ransomware is malware that encrypts victim files and demands payment.",
    "Multi-Factor Authentication (MFA) adds an extra layer of security beyond passwords.",
    "MITRE ATT&CK T1566 refers to Phishing as an initial access technique."
]

collection.add(
    documents=documents,
    ids=[f"doc{i}" for i in range(len(documents))]
)

print("✅ Documents added successfully.")