import os
import json

from langchain.docstore.document import Document

documents = []
for root, dirs, files in os.walk('data/_jsons'):
      for name in files:
        if name.endswith((".json")):
            full_path = os.path.join(root, name)
            with open(full_path, "r") as f:
              data = json.load(f)
              for value in data.values():
                doc = value['content']
                doc =  Document(page_content=value['content'], metadata={"source": full_path, "line_start": value['line_start'], "line_end": value['line_end']})
                documents.append(doc)

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
            indexer = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
            self.index_path = indexer.index(
                index_name=collection_name,
                collection=[d.page_content for d in docs],
                document_metadatas=[d.metadata for d in docs],
                max_document_length=self.chunk_size,
            )

        print(f"Loading index from {self.index_path}...")
        self.retriever = RAGPretrainedModel.from_index(self.index_path)

    def query(self, query: List[str], k: int = 10):
        if self.retriever is None:
            raise ValueError("Collection not built")

        return self.retriever.search(query, k=k)

retriever = ColbertRetriever()
collection_name = "DSA"
retriever.build(documents, collection_name)               