🛡️ AI Cybersecurity Assistant

📌 Project Overview



AI Cybersecurity Assistant is an AI-powered application designed to provide structured explanations of cybersecurity threats and techniques using the MITRE ATT\&CK Enterprise framework.



The system uses Retrieval-Augmented Generation (RAG) with a local Large Language Model to generate context-aware responses from real threat intelligence data.



🎯 Project Objectives



Integrate the MITRE ATT\&CK Enterprise dataset into a searchable knowledge base



Implement a Retrieval-Augmented Generation (RAG) pipeline



Use local LLM inference for privacy and efficiency



Provide structured cybersecurity explanations (Attacker vs Defender perspective)



Build an interactive web interface



🧠 System Architecture



The system follows this pipeline:



User Input (Cybersecurity Question)



Text Embedding Generation



Similarity Search in Vector Database



Context Retrieval



LLM Response Generation



Structured Output Display in UI



🔄 Technologies Used



MITRE ATT\&CK Enterprise Dataset



ChromaDB (Vector Database)



Ollama (Local LLM Runtime)



LLaMA 2 (Language Model)



Streamlit (Web Interface)



⚙️ How It Works (RAG Implementation)

Step 1 – Data Ingestion



The MITRE ATT\&CK JSON dataset is parsed and stored.



Step 2 – Embedding



Each technique description is converted into vector embeddings.



Step 3 – Retrieval



When a user asks a question:



The question is embedded



ChromaDB performs similarity search



The most relevant techniques are retrieved



Step 4 – Generation



The retrieved context is sent to LLaMA2 via Ollama to generate a structured answer.



📊 Structured Output Format



Each response includes:



Technique Name



Technique ID



Description



Attacker Perspective



Defender Perspective



Risk Level



Summary



🧪 Evaluation \& Testing

Test Case 1



Input: “Explain MITRE ATT\&CK technique T1566”

Result: Correct retrieval of Phishing technique with structured explanation.



Test Case 2



Input: “How do attackers use credential dumping?”

Result: Retrieved relevant technique and generated attacker/defender comparison.



Observations



Retrieval accuracy depends on embedding quality



Structured prompting improves answer clarity



Local inference ensures privacy but increases latency



⚠️ Limitations



Dependent on quality of MITRE dataset



Limited by LLaMA2 reasoning capabilities



No automatic quantitative evaluation metric yet



🚀 Future Improvements



Add quantitative evaluation metrics (precision@k)



Improve prompt engineering



Add multi-model comparison



Deploy cloud version



🖥️ How to Run the Project

\# Install dependencies

pip install -r requirements.txt



\# Pull LLaMA2 model via Ollama

ollama pull llama2



\# Run the Streamlit app

streamlit run app.py

📚 Academic Contribution



This project demonstrates practical implementation of:



Retrieval-Augmented Generation (RAG)



Vector similarity search



Local LLM deployment



Applied AI in Cybersecurity



It combines AI system design with real-world threat intelligence frameworks.

