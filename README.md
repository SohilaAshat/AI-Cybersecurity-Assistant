# 🛡️ AI Cybersecurity Assistant

AI Cybersecurity Assistant is an interactive AI‑powered application that uses the
MITRE ATT&CK Enterprise dataset and local LLaMA2 inference via Ollama to provide
structured explanations of cybersecurity techniques and threats.

---

## 🚀 Project Overview

This project lets users ask cybersecurity questions and receive detailed,
structured explanations including threat context, attacker vs defender
perspectives, risk level, and summaries. It uses retrieval‑augmented
generation (ChromaDB) as a fallback for broader context.

---

## 📄 Dataset Summary

This project uses the MITRE ATT&CK Enterprise JSON dataset, which includes
attack techniques with unique IDs (e.g., T1566) and official descriptions.

The dataset is used to provide accurate context when a Cybersecurity Technique
ID is mentioned in the user’s question.

---

## 🔧 Models & Tools Used

| Component | Purpose |
|-----------|---------|
| **LLaMA2 via Ollama CLI** | Local AI reasoning and response generation |
| **ChromaDB** | Vector store for document retrieval |
| **Streamlit** | Web‑based interactive UI |
| **FPDF** | Export conversations as PDF |
| **MITRE ATT&CK JSON** | Official cybersecurity technique data |

---

## 📦 Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/SohilaAshat/AI-Cybersecurity-Assistant.git
cd AI-Cybersecurity-Assistant
Install dependencies:

pip install -r requirements.txt

Ensure the dataset:
Place enterprise-attack.json in the same directory as app.py.

Pull the AI model:

ollama pull llama2

Run the app:

streamlit run app.py
🧠 Usage

Type a question about cybersecurity threats into the input.

Select an explanation level (Beginner, Intermediate, Expert).

Select a mode (Standard, Attacker View, Defender View).

Use suggested questions or enter your own.

Export the conversation to PDF if needed.

💡 Suggested Questions
Question	Level	Mode
Explain MITRE ATT&CK T1566	Beginner	Standard
How does Credential Dumping work?	Intermediate	Attacker View
What is SQL Injection?	Beginner	Standard
Explain Ransomware attack lifecycle	Expert	Defender View
How does Privilege Escalation occur?	Intermediate	Standard
