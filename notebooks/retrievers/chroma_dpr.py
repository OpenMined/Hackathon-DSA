import uuid
from typing import List

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document


class ChromaRetriever:
    def __init__(
        self,
        chunk_size: int = 1024,
        chunk_overlap: int = 100,
        embedder_name: str = "BAAI/bge-small-en-v1.5",
    ):
        self.client = chromadb.PersistentClient()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.embedder_name = embedder_name
        self.collection = None

    def split_docs(self, docs: List[Document]):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
        )
        return text_splitter.split_documents(docs)

    def build(self, docs: List[Document], collection_name: str):
        try:
            self.collection = self.client.get_collection(collection_name)
        except ValueError:
            print("Building collection...")
            docs_split = self.split_docs(docs)
            embedding_fn = SentenceTransformerEmbeddingFunction(
                model_name=self.embedder_name
            )

            self.collection = self.client.create_collection(
                name=collection_name, embedding_function=embedding_fn
            )

            text = [d.page_content for d in docs_split]
            metadatas = [d.metadata for d in docs_split]
            ids = [uuid.uuid4().hex for _ in range(len(docs_split))]

            self.collection.add(
                documents=text,
                metadatas=metadatas,
                ids=ids,
            )

    def query(self, query: List[str], k: int = 10):
        if self.collection is None:
            raise ValueError("Collection not built")
        res = self.collection.query(
            query_texts=query,
            n_results=k,
        )

        return res
