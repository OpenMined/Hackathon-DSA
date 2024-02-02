from pathlib import Path
from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
from ragatouille import RAGPretrainedModel


class ColbertRetriever:
    def __init__(
        self,
        chunk_size: int = 256,
    ):
        self.chunk_size = chunk_size
        self.index_path = None
        self.retriever = None

    def split_docs(self, docs: List[Document]):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap
        )
        return text_splitter.split_documents(docs)

    def build(self, docs: List[Document], collection_name: str):
        self.index_path = f".ragatouille/colbert/indexes/{collection_name}"
        if not Path(self.index_path).exists():
            indexer = RAGPretrainedModel.from_pretrained("/gpfsdswork/dataset/HuggingFace_Models/colbert-ir/colbertv2.0/")
            self.index_path = indexer.index(
                index_name=collection_name,
                collection=[d.page_content for d in docs],
                document_metadatas=[d.metadata for d in docs],
                max_document_length=self.chunk_size,
            )

        print(f"Loading index from {self.index_path}...")
        self.retriever = RAGPretrainedModel.from_index(self.index_path)
        # self.retriever = indexer

    def query(self, query: List[str], k: int = 10):
        if self.retriever is None:
            raise ValueError("Collection not built")

        return self.retriever.search(query, k=k, index_name="DSA")
