# 🛡️ AI Cybersecurity Assistant

This repository contains an interactive AI-powered cybersecurity assistant designed to explain, analyze, and reason about security threats using structured knowledge and retrieval-augmented generation. It leverages the MITRE ATT&CK Enterprise dataset, a vector database (ChromaDB), and local LLaMA2 inference via Ollama to provide detailed and customizable explanations.

---

An \*\*interactive AI-powered cybersecurity assistant\*\* that provides structured explanations of MITRE ATT\&CK techniques and general cybersecurity concepts.  

Built with \*\*Streamlit\*\*, \*\*LLaMA2 via Ollama\*\*, and \*\*ChromaDB\*\*.



---



\## Repository Structure



| Folder / File | Description |

|---------------|-------------|

| `app.py` | Main Streamlit app integrating MITRE ATT\&CK, ChromaDB, and LLaMA2. |

| `enterprise-attack.json` | MITRE ATT\&CK Enterprise dataset for technique descriptions. |

| `requirements.txt` | Python dependencies: Streamlit, FPDF, ChromaDB, etc. |



---



\##  Features \& Learning Path



\### Part 1: Foundational Setup

\-  \*\*MITRE ATT\&CK Integration:\*\* Load JSON dataset for technique lookups (e.g., T1566).  

\-  \*\*ChromaDB Retrieval:\*\* Fetch external cybersecurity documents if question not in MITRE dataset.  

\-  \*\*Streamlit UI:\*\* Interactive interface with text input, suggested questions, and sidebar settings.  



\### Part 2: AI Explanation Modes

\-  \*\*Explanation Levels:\*\* Beginner | Intermediate | Expert  

\-  \*\*Modes:\*\* Standard | Attacker View | Defender View  

\-  \*\*Generated Sections per Answer:\*\*

&nbsp; 1. Threat Explanation  

&nbsp; 2. Attacker Perspective \*(if mode allows)\*  

&nbsp; 3. Defender Perspective \*(if mode allows)\*  

&nbsp; 4. Risk Level (Low / Medium / High)  

&nbsp; 5. Short Summary for learners  



\### Part 3: Conversation \& Evaluation

\-  \*\*Conversation History:\*\* Tracks questions and AI answers.  

\-  \*\*Evaluation Sliders:\*\* Rate Clarity, Consistency, Usefulness.  

\-  \*\*Suggested Questions:\*\* Quick access to common cybersecurity inquiries.



\### Part 4: Export \& Reporting

\-  \*\*PDF Export:\*\* Save conversation with evaluations.  

\-  \*\*Keyword Highlighting:\*\* Auto-bold terms like \*\*Phishing\*\*, \*\*Ransomware\*\*, \*\*SQL Injection\*\*, etc.



\### Part 5: UI Customization

\-  \*\*Theme Options:\*\* Light \& Dark modes.  

\-  \*\*Responsive Layout:\*\* Adaptive columns for suggested questions \& sliders.



---



\##  Installation \& Setup



```bash

\# Clone repository

git clone https://github.com/<your\_username>/AI-Cybersecurity-Assistant.git

cd AI-Cybersecurity-Assistant



\# Install dependencies

pip install -r requirements.txt

Download MITRE ATT\&CK JSON dataset

Save enterprise-attack.json in the project root.

Official JSON: MITRE ATT\&CK Enterprise



Set up Ollama LLaMA2 model



ollama pull llama2



Run Streamlit app



streamlit run app.py

💬 Suggested Questions

Question	                                                         Level	             Mode

Explain MITRE ATT\&CK T1566	                      Beginner	            Standard

How does Credential Dumping work?  	     Intermediate	            Attacker View

What is SQL Injection?	                                     Beginner	            Standard

Explain Ransomware attack lifecycle	     Expert	            Defender View

How does Privilege Escalation occur?	     Intermediate	            Standard



Click a suggested question in the app to automatically populate the input box.

