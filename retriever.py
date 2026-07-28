from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embeddings


def get_retriever():

    db = FAISS.load_local(
        "faiss_index",
        get_embeddings(),
        allow_dangerous_deserialization=True
    )
    return db.as_retriever(
        search_kwargs={"k":3}
    )