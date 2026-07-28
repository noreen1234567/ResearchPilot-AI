# 🔬 ResearchPilot AI
### Autonomous Research Intelligence Agent

ResearchPilot AI is an AI-powered research assistant that helps researchers, students, and professionals analyze academic research papers efficiently.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded research papers and generate accurate, context-aware responses using a local Large Language Model (LLM).

---

## 🚀 Features

- 📄 Upload and analyze research papers (PDF)
- 🤖 AI-powered question answering
- 🔍 Retrieval-Augmented Generation (RAG)
- 📚 Automatic literature review generation
- 💡 Future research direction suggestions
- 🔎 Research gap detection
- ⚡ Fast semantic search using FAISS
- 🔒 Fully local AI processing with Ollama

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- Qwen2.5 (Local LLM)
- nomic-embed-text Embeddings
- FAISS Vector Database
- PyPDF
- Retrieval-Augmented Generation (RAG)

---

## ⚙️ System Workflow

1. Upload a research paper in PDF format.
2. Extract text from the PDF.
3. Split the document into smaller chunks.
4. Generate vector embeddings using **nomic-embed-text**.
5. Store embeddings in a **FAISS Vector Database**.
6. Retrieve the most relevant document chunks using RAG.
7. Generate accurate, context-aware answers with the local **Qwen2.5** model.

---

## 📂 Project Structure

```text
ResearchPilot-AI/
│
├── agents/
│   └── research_agent.py
│
├── rag/
│   ├── embeddings.py
│   ├── retriever.py
│   └── vector_store.py
│
├── tools/
│   └── pdf_loader.py
│
├── data/
│   └── uploads/
│
├── static/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## 📸 Key Features

- Research Paper Analysis
- Context-Aware AI Question Answering
- Literature Review Generation
- Future Research Suggestions
- Research Gap Detection
- Semantic Search with FAISS
- Local AI using Ollama

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ResearchPilot-AI.git
cd ResearchPilot-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Required Ollama Models

```bash
ollama pull qwen2.5:0.5b
ollama pull nomic-embed-text
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Launch the application.
2. Upload a research paper (PDF).
3. Wait for the knowledge base to be created.
4. Ask questions about the paper.
5. Generate:
   - Literature Review
   - Future Research Directions
   - Research Gap Analysis

---

## 🎯 Applications

- Academic Research
- Literature Review
- Research Paper Analysis
- Thesis & Final Year Projects
- AI-assisted Learning
- Scientific Document Exploration

---

## 🌟 Future Improvements

- Multi-document comparison
- Web search integration
- Research paper summarization dashboard
- Citation generation
- Support for DOCX and TXT documents
- Multi-agent research workflow
- MCP integration
- n8n automation workflow

---

## 👨‍💻 Developed By

**Noreen Shahzad**

BS Artificial Intelligence

---

## 📄 License

This project is developed for educational and research purposes.
