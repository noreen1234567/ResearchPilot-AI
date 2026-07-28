import traceback
import streamlit as st

from agents.research_agent import ask_ai
from tools.pdf_loader import extract_text_from_pdf
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ResearchPilot AI",
    page_icon="🔬",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
color:white;
}

/* Hide Streamlit Menu */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Hero Card */

.hero{
background:rgba(255,255,255,.07);
border:1px solid rgba(255,255,255,.12);
padding:35px;
border-radius:22px;
backdrop-filter:blur(12px);
animation:fade 1.2s ease;
}

.title{
font-size:48px;
font-weight:bold;
text-align:center;
color:#4ADE80;
animation:glow 2s infinite alternate;
}

.subtitle{
text-align:center;
font-size:20px;
color:#d1d5db;
margin-bottom:15px;
}

.about{
font-size:17px;
line-height:1.8;
color:#e5e7eb;
}

/* Cards */

.card{
background:#1f2937;
padding:18px;
border-radius:16px;
text-align:center;
transition:.3s;
margin-top:10px;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0px 0px 20px rgba(74,222,128,.4);
}

/* Upload Box */

section[data-testid="stFileUploader"]{
background:#1f2937;
padding:15px;
border-radius:15px;
}

/* Animation */

@keyframes fade{

from{
opacity:0;
transform:translateY(40px);
}

to{
opacity:1;
transform:translateY(0px);
}

}

@keyframes glow{

from{
text-shadow:0px 0px 8px #4ADE80;
}

to{
text-shadow:0px 0px 30px #4ADE80;
}

}

</style>
""",unsafe_allow_html=True)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""

<div class="hero">

<div class="title">
🔬 ResearchPilot AI
</div>

<div class="subtitle">
Autonomous Research Intelligence Agent
</div>

<hr>

<div class="about">

ResearchPilot AI is an intelligent AI-powered research assistant designed
to help researchers, students and professionals understand academic papers.

The system combines

<b>Retrieval-Augmented Generation (RAG)</b>,
<b>FAISS Vector Database</b>,
<b>LangChain</b>,
<b>Ollama Local LLM</b>

to generate accurate context-aware answers from uploaded research papers.

</div>

</div>

""",unsafe_allow_html=True)

st.write("")

st.caption("🚀 Transforming Research Papers into Actionable Knowledge using AI")
# ==========================================
# FEATURE CARDS
# ==========================================

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
<div class="card">

📄

### Research Analysis

Analyze Research Papers

</div>
""",unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="card">

🔍

### Semantic Search

RAG + FAISS

</div>
""",unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="card">

🤖

### AI Assistant

Context Aware Answers

</div>
""",unsafe_allow_html=True)

col4,col5,col6=st.columns(3)

with col4:

    st.markdown("""
<div class="card">

📚

### Literature Review

Automatic Review

</div>
""",unsafe_allow_html=True)

with col5:

    st.markdown("""
<div class="card">

💡

### Future Research

Research Suggestions

</div>
""",unsafe_allow_html=True)

with col6:

    st.markdown("""
<div class="card">

🔎

### Research Gaps

Gap Detection

</div>
""",unsafe_allow_html=True)

st.divider()

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)

    st.title("ResearchPilot AI")

    st.markdown("""
<div style="
background:linear-gradient(90deg,#16a34a,#22c55e);
padding:12px;
border-radius:12px;
text-align:center;
color:white;
font-size:18px;
font-weight:bold;
margin-bottom:15px;
">
🟢 AI System Online
</div>
""", unsafe_allow_html=True)

    st.info("""
Model :
**Qwen2.5 (Ollama)**

Embeddings :
**nomic-embed-text**

Vector Database :
**FAISS**
""")

    st.markdown("---")

    st.markdown("### 🛠 Technologies")

    st.markdown("""
- Python
- Streamlit
- LangChain
- Ollama
- FAISS
- RAG
- PyPDF
""")

st.caption("Version 1.0")

st.markdown("---")

st.markdown("### 📊 Project Statistics")

st.metric("AI Model", "Qwen2.5")
st.metric("Vector DB", "FAISS")
st.metric("RAG", "Enabled")

# ==========================================
# PDF Upload
# ==========================================

st.markdown("## 📄 Upload Research Paper")

uploaded_file = st.file_uploader(
    "Choose a Research Paper (PDF)",
    type=["pdf"]
)

retriever = None
pdf_text = ""

if uploaded_file is not None:

    with st.spinner("📖 Reading PDF..."):

        pdf_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🧠 Creating Knowledge Base..."):

        create_vector_store(pdf_text)

        retriever = get_retriever()

    st.success("✅ Research Paper Indexed Successfully!")

    st.info(f"""
📄 **Paper Name:** {uploaded_file.name}

🧠 Knowledge Base Created Successfully

⚡ Ready for AI-powered Question Answering
""")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Pages Loaded",
            len(pdf_text.split("\n"))
        )

    with col2:
        st.metric(
            "Characters",
            len(pdf_text)
        )

    with st.expander("📄 Preview Extracted Text"):

        st.write(pdf_text[:3500])

st.divider()


# ==========================================
# ASK QUESTION
# ==========================================

st.markdown("## 🤖 Ask ResearchPilot AI")

question = st.text_area(
    "Ask anything about your uploaded research paper",
    placeholder="Example : What is the main contribution of this paper?"
)

if st.button(
    "🚀 Ask AI",
    use_container_width=True
):

    if uploaded_file is None:

        st.warning("Please upload a research paper first.")

    elif question.strip() == "":

        st.warning("Please enter your question.")

    else:

        try:

            docs = retriever.invoke(question)

            context = "\n\n".join(
                [doc.page_content for doc in docs]
            )

            prompt = f"""
You are an expert AI Research Assistant.

Answer ONLY from the context below.

Never invent facts.

If the answer is not available in the paper, say:

'I could not find this information in the uploaded research paper.'

Context:

{context}

Question:

{question}
"""

            answer = ask_ai(prompt)

            st.success("✅ Answer Generated Successfully!")

            st.markdown("### 🤖 AI Response")

            st.write(answer)

        except Exception:

            st.error(traceback.format_exc())

st.divider()

# ==========================================
# AI RESEARCH TOOLS
# ==========================================

st.markdown("## 🧠 AI Research Tools")

col1, col2, col3 = st.columns(3)

with col1:
    literature_btn = st.button(
        "📚 Literature Review",
        use_container_width=True
    )

with col2:
    future_btn = st.button(
        "💡 Future Research",
        use_container_width=True
    )

with col3:
    gap_btn = st.button(
        "🔎 Research Gap Detection",
        use_container_width=True
    )

st.divider()


# ==========================================
# LITERATURE REVIEW
# ==========================================

if literature_btn:

    if uploaded_file is None:

        st.warning("Please upload a research paper first.")

    else:

        try:

            with st.spinner("Generating Literature Review..."):

                docs = retriever.invoke("Summarize this research paper")

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                prompt = f"""
You are an AI Research Expert.

Using ONLY the context below, generate a professional literature review.

Context:
{context}

Include:

1. Research Background
2. Existing Work
3. Main Contribution
4. Strengths
5. Limitations

Write in academic English.
"""

                answer = ask_ai(prompt)

            st.success("✅ Literature Review Generated")

            st.markdown("## 📚 Literature Review")

            st.info(answer)

        except Exception:

            st.error(traceback.format_exc())


# ==========================================
# FUTURE RESEARCH
# ==========================================

if future_btn:

    if uploaded_file is None:

        st.warning("Please upload a research paper first.")

    else:

        try:

            with st.spinner("Finding Future Research Directions..."):

                docs = retriever.invoke("future work limitations")

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                prompt = f"""
Based ONLY on the context below suggest:

- Future Research Directions
- Possible Improvements
- Open Challenges

Context:

{context}
"""

                answer = ask_ai(prompt)

            st.success("✅ Future Research Generated")

            st.markdown("## 💡 Future Research")

            st.success(answer)

        except Exception:

            st.error(traceback.format_exc())


# ==========================================
# RESEARCH GAP DETECTION
# ==========================================

if gap_btn:

    if uploaded_file is None:

        st.warning("Please upload a research paper first.")

    else:

        try:

            with st.spinner("Detecting Research Gaps..."):

                docs = retriever.invoke("limitations challenges")

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )

                prompt = f"""
You are an AI Research Analyst.

Using ONLY this context identify:

- Research Gaps
- Current Limitations
- Open Challenges
- Suggested Improvements

Context:

{context}
"""

                answer = ask_ai(prompt)

            st.success("✅ Research Gap Analysis Completed")

            st.markdown("## 🔎 Research Gap Analysis")

            st.warning(answer)

        except Exception:

            st.error(traceback.format_exc())

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <center>

    ---
    🔬 <b>ResearchPilot AI</b><br>

    Autonomous Research Intelligence Agent<br><br>

    Built with ❤️ using
    <b>Python • Streamlit • LangChain • FAISS • Ollama • RAG</b>

    </center>
    """,
    unsafe_allow_html=True
)

