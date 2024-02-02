import sys
import csv
import os
from translation import Translator
from retrievers.chroma_dpr import ChromaRetriever
# from retrievers.colbert import ColbertRetriever

import langdetect
from collections import Counter
from pathlib import Path
from pprint import pprint

DATA_DIR = Path("/Users/koen/workspace/Hackathon-DSA/data")
# SNAPSHOTS_DIR = DATA_DIR / "platform-docs-snapshots"
VERSIONS_DIR = DATA_DIR / "platform-docs-versions"

from langchain_community.document_loaders import UnstructuredMarkdownLoader, DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def translate_questions(questions):
    translator = Translator()

    src_langs = []
    for question in questions:
        translated, src_lang = translator.translate(question['question'], "en")
        question['question'] = translated
        src_langs.append(src_lang)
    return questions, src_langs

def translate_answers(answers, src_langs):
    translator = Translator()

    for answer, src_lang in zip(answers, src_langs):
        translated, _ = translator.translate(answer, src_lang)
        answer = translated
    return answers

def answer_query(query, retriever, rag_generator):
    k = 3
    results = retriever.query(query['question'], k)
    context = [r['content'] for r in results]
    print()
    chat_logs = rag_generator.generate_answer(context, query["question"])
    # chat_logs = rag_generator.generate_batch(context, query['question'])
    answer = chat_logs[-1]["content"]
    prompt = chat_logs[-1]["prompt"]
    top_result = results[0]
    source = top_result["document_metadata"].get("url", '')

    return answer, prompt, source

def generate_answers(queries, retriever, rag_generator):
    answers = []
    prompts = []
    sources = []

    for query in queries:
        print(query)
        answer, prompt, source = answer_query(query, retriever, rag_generator)

        answers.append({"id": query['id'], "content": answer})
        prompts.append({"id": query['id'], "content": prompt})
        sources.append({"id": query['id'], "content": source})

    return answers, prompts, sources

def write_output(output_dir, output, type):
    with open(f"{output_dir}/{type}/{output['id']}.txt", "w") as f:
        f.write(output['content'])

def prep_retrieval():
    docs = DirectoryLoader(VERSIONS_DIR, glob="[!.]*/[!.]*.md", loader_cls=TextLoader).load()
    docs = [d for d in docs if Path(d.metadata['source']) != VERSIONS_DIR / "README.md"]

    languages = [langdetect.detect(d.page_content) for d in docs]

    for doc, language in zip(docs, languages):
        doc.metadata["language"] = language

    print(Counter(languages))

    # from retrievers.chroma_dpr import ChromaRetriever
    # import re

    # retriever = ChromaRetriever()
    from retrievers.colbert import ColbertRetriever
    retriever = ColbertRetriever()
    collection_name = "DSA"
    retriever.build(docs, collection_name)
    return retriever

def prep_generator():
    from generators.mistral import MistralRAGGenerator

    rag_generator = MistralRAGGenerator()

    return rag_generator

if __name__ == "__main__":
    print("STARTING PREPARATION...")
    retriever = prep_retrieval()
    print("RETRIEVAL LOADED!")
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

    print("TRANSLATING QUESTIONS")
    questions, source_languages = translate_questions(questions)
    
    print("GENERATING ANSWERS...")
    answers, prompts, sources = generate_answers(
        questions, 
        retriever, 
        rag_generator)
    print("GENERATION FINISHED!")

    print("TRANSLATING ANSWERS...")
    answers = translate_answers(answers, source_languages)

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

