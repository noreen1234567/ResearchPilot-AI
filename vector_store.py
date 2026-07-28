from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from rag.embeddings import get_embeddings


def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    db = FAISS.from_documents(
        documents,
        get_embeddings()
    )

    db.save_local("faiss_index")

    return db