"""
Enterprise RAG pipeline featuring metadata-aware document retrieval and grounded synthesis.
"""

from typing import List, Dict
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class EnterpriseRAGPipeline:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.vector_store = None

    def ingest_documents(self, documents: List[Dict[str, str]]):
        """Ingests documents with classification metadata and access tags."""
        docs = [
            Document(
                page_content=item["content"],
                metadata={
                    "doc_id": item["id"],
                    "department": item["department"],
                    "access_level": item["access_level"]
                }
            )
            for item in documents
        ]
        self.vector_store = FAISS.from_documents(docs, self.embeddings)

    def retrieve(self, query: str, user_access_level: str, top_k: int = 3) -> List[Document]:
        """
        Retrieves context with metadata-based security filtering.
        """
        if not self.vector_store:
            raise ValueError("Vector store is uninitialized. Ingest documents first.")

        # Filter documents based on role/access level
        retriever = self.vector_store.as_retriever(
            search_kwargs={
                "k": top_k,
                "filter": {"access_level": user_access_level}
            }
        )
        return retriever.invoke(query)
