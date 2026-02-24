🛡️ AI Cybersecurity Assistant

AI Cybersecurity Assistant is an interactive application that uses the MITRE ATT&CK dataset and AI (LLaMA2 via Ollama) to provide structured educational answers to cybersecurity questions.

🚀 Project Overview

Offers explanations for attack and defense techniques in cybersecurity.

Shows Threat Explanation, Attacker Perspective, Defender Perspective, and Risk Level.

Conversations can be exported as PDF for reference.

📂 Project Contents

app.py – main Streamlit application

enterprise-attack.json – MITRE ATT&CK dataset

chroma_db/ – optional storage for RAG (Retrieval-Augmented Generation)

Dependencies: FPDF, ChromaDB, Streamlit, Subprocess

📝 Dataset Summary

MITRE ATT&CK Enterprise dataset: includes attack techniques, Technique IDs (TIDs), and official descriptions.

Used for quick lookup of techniques and providing accurate context in answers.

⚙️ Models & Tools

LLaMA2 via Ollama CLI for generating AI explanations.

ChromaDB for document retrieval when a technique is not directly matched.

Streamlit for building the interactive user interface.

FPDF for exporting conversation logs to PDF.

🛠️ How to Run the Demo

Clone the repository:

git clone https://github.com/SohilaAshat/AI-Cybersecurity-Assistant.git
cd AI-Cybersecurity-Assistant

Install dependencies:

pip install -r requirements.txt

If requirements.txt is not available, install manually:

pip install streamlit fpdf chromadb

Ensure dataset is present:

Place enterprise-attack.json in the same folder as app.py.

Run the application:

streamlit run app.py

Using the interface:

Type your question in the input box.

Use Suggested Questions for quick examples.

Choose Theme, Explanation Level, and Mode in the sidebar.

Exporting conversation:

Click Export Conversation to PDF after your chat to download a log.
