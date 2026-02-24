# app.py 
import streamlit as st
from io import BytesIO
from fpdf import FPDF
import chromadb
import subprocess
import json

# ==============================
# Load MITRE ATT&CK dataset
# ==============================
with open("enterprise-attack.json", "r", encoding="utf-8") as f:
    attack_data = json.load(f)

techniques_dict = {}
for obj in attack_data.get("objects", []):
    if obj.get("type") == "attack-pattern":
        tid = obj.get("external_references", [{}])[0].get("external_id")
        name = obj.get("name")
        desc = obj.get("description", "")
        if tid:
            techniques_dict[tid] = {"name": name, "description": desc}

# ==============================
# Caching for ChromaDB retrieval
# ==============================
@st.cache_data(show_spinner=False)
def retrieve_docs(question):
    client = chromadb.Client(
        settings=chromadb.config.Settings(
            persist_directory="chroma_db",
            is_persistent=True
        )
    )
    collection = client.get_collection("cybersecurity_docs")
    results = collection.query(
        query_texts=[question],
        n_results=5,
        include=["documents", "metadatas"]
    )
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0] if results.get("metadatas") else [{}]*len(documents)
    return documents, metadatas

# ==============================
# Caching for LLaMA2 response
# ==============================
@st.cache_data(show_spinner=False)
def generate_answer(prompt):
    response = subprocess.run(
        ["ollama", "run", "llama2", prompt],
        capture_output=True,
        text=True
    )
    return response.stdout.strip()

# ==============================
# Main Get Answer Function
# ==============================
def get_answer(question, level, mode):
    try:
        #  Check if Technique ID is in question
        found_tid = next((tid for tid in techniques_dict if tid.lower() in question.lower()), None)

        if found_tid:
            base_info = techniques_dict[found_tid]
            prompt = f"""
You are a cybersecurity expert.

Technique: {found_tid} - {base_info['name']}
Official Description: {base_info['description']}

Mode: {mode}
Explanation Level: {level}

Create a structured educational explanation based on the official description.
Include:
1. Threat Explanation
2. Attacker Perspective (if mode allows)
3. Defender Perspective (if mode allows)
4. Risk Level (Low / Medium / High)
5. Short Summary for learners
"""
        else:
            #  Use ChromaDB retrieval
            documents, metadatas = retrieve_docs(question)
            retrieved_docs = ""
            for i, doc in enumerate(documents):
                meta = metadatas[i] if metadatas and i < len(metadatas) else {}
                tech_id = meta.get("technique_id", "Unknown")
                tech_name = meta.get("technique_name", "Unknown")
                retrieved_docs += f"\n[Technique: {tech_id} - {tech_name}]\n{doc}\n"
            if not retrieved_docs.strip():
                retrieved_docs = "No relevant context found in MITRE dataset."

            prompt = f"""
You are a cybersecurity expert.

Mode: {mode}
Explanation Level: {level}

Context:
{retrieved_docs}

Question:
{question}

Provide a structured educational explanation.
"""

        #  Generate answer via LLaMA2
        answer = generate_answer(prompt)
        if not answer:
            return " The AI did not return a response. Try rephrasing the question."
        return answer

    except Exception as e:
        return f" Error retrieving answer: {e}"

# ==============================
# Streamlit Page Setup
# ==============================
st.set_page_config(page_title="AI Cybersecurity Assistant", layout="wide")

st.sidebar.title("Settings")
theme = st.sidebar.radio("Theme:", ["Light", "Dark"])
level = st.sidebar.selectbox("Explanation level:", ["Beginner", "Intermediate", "Expert"])
mode = st.sidebar.selectbox("Mode:", ["Standard", "Attacker View", "Defender View"])

suggested_questions = [
    "Explain MITRE ATT&CK T1566",
    "How does Credential Dumping work?",
    "What is SQL Injection?",
    "How does Privilege Escalation occur?",
    "Explain Ransomware attack lifecycle"
]

if theme == "Dark":
    st.markdown("""
        <style>
        .reportview-container, .main, .block-container {background-color: #0e1117; color: #f5f5f5;}
        .stTextInput>div>div>input {background-color: #1c1f26; color: #f5f5f5;}
        .stButton>button {background-color: #2e3340; color: #f5f5f5;}
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .reportview-container, .main, .block-container {background-color: #ffffff; color: #0c0c0c;}
        .stTextInput>div>div>input {background-color: #f0f0f0; color: #0c0c0c;}
        .stButton>button {background-color: #e0e0e0; color: #0c0c0c;}
        </style>
        """, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

st.title("🛡️ AI Cybersecurity Assistant")
st.write("Ask a cybersecurity question based on MITRE ATT&CK dataset:")

user_input = st.text_input("Your question:", st.session_state.user_input)
st.session_state.user_input = user_input

st.subheader("Suggested Questions")
cols = st.columns(len(suggested_questions))
for i, q in enumerate(suggested_questions):
    if cols[i].button(q):
        st.session_state.user_input = q
        user_input = q

if st.button("Ask") and user_input.strip() != "":
    ai_response = get_answer(user_input, level, mode)
    st.session_state.conversation.append({
        "user": user_input,
        "ai": ai_response,
        "evaluation": {"clarity":3,"consistency":3,"usefulness":3}
    })

st.subheader("Conversation History")
for idx, msg in enumerate(st.session_state.conversation):
    with st.expander(f"Q: {msg['user']}", expanded=True):
        answer = msg['ai']
        for keyword in ["Phishing", "Ransomware", "MFA", "SQL Injection"]:
            if answer:
                answer = answer.replace(keyword, f"**{keyword}**")
        st.markdown(f"A: {answer}")

        col1, col2, col3 = st.columns([1,1,1])
        clarity = col1.slider("Clarity", 1, 5, msg["evaluation"]["clarity"], key=f"clarity_{idx}")
        consistency = col2.slider("Consistency", 1, 5, msg["evaluation"]["consistency"], key=f"consistency_{idx}")
        usefulness = col3.slider("Usefulness", 1, 5, msg["evaluation"]["usefulness"], key=f"usefulness_{idx}")

        st.session_state.conversation[idx]["evaluation"] = {
            "clarity": clarity, "consistency": consistency, "usefulness": usefulness
        }

# ==============================
# Export to PDF
# ==============================
def export_pdf(conversation):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "AI Cybersecurity Assistant Conversation", ln=True, align="C")
    pdf.ln(5)
    for msg in conversation:
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, f"Q: {msg['user']}")
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, f"A: {msg['ai']}")
        eval_str = f"Clarity: {msg['evaluation']['clarity']}/5 | Consistency: {msg['evaluation']['consistency']}/5 | Usefulness: {msg['evaluation']['usefulness']}/5"
        pdf.multi_cell(0, 8, eval_str)
        pdf.ln(3)
    return pdf.output(dest='S').encode('latin1')

if st.button("Export Conversation to PDF"):
    if st.session_state.conversation:
        pdf_bytes = export_pdf(st.session_state.conversation)
        st.download_button("Download PDF", data=pdf_bytes, file_name="conversation.pdf", mime="application/pdf")
    else:
        st.warning("No conversation to export yet.")