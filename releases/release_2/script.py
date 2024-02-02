import sys
import csv
import os
from retrievers.chroma_dpr import ChromaRetriever

import langdetect
from collections import Counter
from pathlib import Path
from pprint import pprint

DATA_DIR = Path("/gpfswork/rech/jft/uhp49nn/data")
# SNAPSHOTS_DIR = DATA_DIR / "platform-docs-snapshots"
VERSIONS_DIR = DATA_DIR / "platform-docs-versions"

from langchain_community.document_loaders import UnstructuredMarkdownLoader, DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def answer_query(query, retriever, rag_generator):
    k = 5
    results = retriever.query(query['content'], k)
    context = results["documents"]
    chat_logs = rag_generator.generate_batch(context, query['content'])
    answer = [c[-1]["content"] for c in chat_logs]
    prompt = [c[-1]["prompt"] for c in chat_logs]
    source = ''

    return answer, prompt, source

def generate_answers(queries, retriever, rag_generator):
    answers = []
    prompts = []
    sources = []

    for query in queries:
        answer, prompt, source = answer_query(query, retriever, rag_generator)

        answers.append({"id": query['id'], "content": answer})
        prompts.append({"id": query['id'], "content": prompt})
        sources.append({"id": query['id'], "content": source})

    return answers, prompts, sources

def write_output(output_dir, output, type):
    with open(f"{output_dir}/{type}/{output['id']}.txt", "w") as f:
        f.write(output['content'])

def prep_retrieval():
    import os
    import json

    from langchain.docstore.document import Document

    documents = []
    for root, dirs, files in os.walk('../../data/_jsons'):
        for name in files:
            if name.endswith((".json")):
                full_path = os.path.join(root, name)
                with open(full_path, "r") as f:
                    data = json.load(f)
                    for value in data.values():
                        doc = value['content']
                        doc =  Document(page_content=value['content'], metadata={"source": full_path, "line_start": value['line_start'], "line_end": value['line_end']})
                        documents.append(doc)

    languages = [langdetect.detect(d.page_content) for d in documents]

    for doc, language in zip(documents, languages):
        doc.metadata["language"] = language

    print(Counter(languages))

    retriever = ChromaRetriever()
    # from retrievers.colbert import ColbertRetriever
    # retriever = ColbertRetriever()
    collection_name = "DSA"
    retriever.build(documents, collection_name)
    return retriever

def prep_generator():
    from generators.mistral import MistralRAGGenerator

    rag_generator = MistralRAGGenerator()

    return rag_generator

if __name__ == "__main__":
    print("STARTING PREPARATION...")
    retriever = prep_retrieval()
    rag_generator = prep_generator()
    print("PREPARATION FINISHED!")

    input_file_path = sys.argv[1]
    output_dir_path = sys.argv[2]

    questions = []

    print("READING QUESTIONS...")
    with open(input_file_path) as csvfile:
        question_reader = csv.DictReader(csvfile, delimiter=';')
        for row in question_reader:
            questions.append(row)
    print("READING FINISHED!")
    
    print("GENERATING ANSWERS...")
    answers, prompts, sources = generate_answers(
        questions[:1], 
        retriever, 
        rag_generator)
    print("GENERATION FINISHED!")

    print("WRITING ANSWERS...")
    if not os.path.exists(f"{output_dir_path}/prompts"):
        os.mkdir(f"{output_dir_path}/prompts")
    if not os.path.exists(f"{output_dir_path}/answers"):
        os.mkdir(f"{output_dir_path}/answers")
    if not os.path.exists(f"{output_dir_path}/sources"):
        os.mkdir(f"{output_dir_path}/sources")

    for answer in answers:
        write_output(output_dir_path, answer, "answers")

    for prompt in prompts:
        write_output(output_dir_path, prompt, "prompts")

    for source in sources:
        write_output(output_dir_path, source, "sources")
    print("WRITING FINISHED!")

    print("DONE")

