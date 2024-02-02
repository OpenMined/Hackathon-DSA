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


retriever = ColbertRetriever()
collection_name = "DSA"
retriever.build(documents, collection_name)               