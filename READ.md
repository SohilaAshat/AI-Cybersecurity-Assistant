AI Cybersecurity Assistant

A Retrieval-Augmented Generation Approach for MITRE ATT\&CK-Based Threat Explanation

Abstract



This project presents an AI-powered Cybersecurity Assistant that leverages Retrieval-Augmented Generation (RAG) to provide structured explanations of cyber threats using the MITRE ATT\&CK Enterprise framework.



The system integrates vector similarity search with local Large Language Model (LLM) inference to deliver context-aware responses, including attacker and defender perspectives. The architecture combines structured threat intelligence with generative AI to create an explainable cybersecurity reference tool.



1\. Introduction



Modern cybersecurity analysis requires structured understanding of adversarial techniques. The MITRE ATT\&CK framework provides a comprehensive knowledge base of adversary tactics and techniques. However, navigating large JSON datasets can be complex for learners and analysts.



This project proposes an AI-driven assistant that enables natural language interaction with the MITRE ATT\&CK dataset using a Retrieval-Augmented Generation (RAG) pipeline. The system retrieves relevant techniques and generates structured explanations through a local LLM.



2\. Related Technologies



The system integrates the following technologies:



MITRE ATT\&CK Enterprise Dataset



ChromaDB for vector similarity search



Ollama for local model inference



LLaMA 2 as the generative model



Streamlit for the interactive web interface



3\. System Architecture



The system follows a Retrieval-Augmented Generation architecture consisting of:



3.1 Data Ingestion



The MITRE ATT\&CK Enterprise JSON dataset is parsed and preprocessed. Technique descriptions are extracted and prepared for embedding.



3.2 Embedding \& Vector Storage



Each technique description is converted into high-dimensional vector embeddings and stored in ChromaDB for similarity search.



3.3 Retrieval Phase



When a user submits a query:



The query is embedded.



Vector similarity search retrieves the most relevant techniques.



Retrieved context is aggregated.



3.4 Generation Phase



The retrieved context is passed to LLaMA2 via Ollama.

A structured prompt ensures the output contains:



Technique Name



Technique ID



Description



Attacker Perspective



Defender Perspective



Risk Level



Summary



3.5 User Interface



The system is deployed via Streamlit, enabling interactive question-answering.



4\. Methodology



The project implements Retrieval-Augmented Generation to overcome limitations of standalone LLMs. Instead of relying solely on model memory, the assistant retrieves verified threat intelligence before generation.



The workflow can be summarized as:



User Query → Embedding → Similarity Search → Context Retrieval → Prompt Construction → LLM Generation → Structured Output



This architecture improves factual grounding and reduces hallucination risk.



5\. Experimental Evaluation

Test Case 1



Input: "Explain MITRE ATT\&CK technique T1566"

Result: Correct retrieval of the Phishing technique and structured explanation including attacker and defender insights.



Test Case 2



Input: "How do attackers perform credential dumping?"

Result: Relevant technique retrieved with accurate contextual explanation.



Observations



Retrieval quality directly impacts response accuracy.



Structured prompting improves consistency of output format.



Local inference ensures privacy but introduces moderate latency.



6\. Limitations



No quantitative metric (e.g., precision@k) implemented.



Performance depends on embedding quality.



LLM reasoning is limited by model size.



No adversarial robustness testing performed.



7\. Future Work



Implement automated evaluation metrics



Compare multiple embedding models



Add multi-model LLM comparison



Deploy scalable cloud version



Add feedback-based reinforcement mechanism



8\. Conclusion



This project demonstrates a practical implementation of Retrieval-Augmented Generation for cybersecurity knowledge exploration. By integrating the MITRE ATT\&CK framework with vector similarity search and local LLM inference, the system provides structured, explainable cybersecurity insights.



The work highlights the effectiveness of combining retrieval systems with generative models for domain-specific AI applications.

