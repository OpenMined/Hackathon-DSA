# !pip install llama-cpp-python langchain langdetect

from llama_cpp import Llama
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import langdetect

DATA_DIR = Path("../data")
SNAPSHOTS_DIR = DATA_DIR / "platform-docs-snapshots"
VERSIONS_DIR = DATA_DIR / "platform-docs-versions"


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024, chunk_overlap=0
)

llm = Llama(
    model_path="../models/towerinstruct-7b-v0.1.Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=8,
    n_gpu_layers=0,
    chat_format="chatml",
)


SYSTEM_PROMPT="""
You are an assistant that translates technical markdown documentation from french to english.
- French documentation is fed to you in chunks, the only thing you answer is a english translation
- Subsequent chunks are all from the same document
- If the provided contains just random characters (like an embedded image), you omit this part.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024, chunk_overlap=0
)


def translate(split, chat_log=None):
    if not chat_log:
        chat_log = [{"role": "system", "content": SYSTEM_PROMPT}]
    chat_log.append({"role": "user", "content": split})
    answer = llm.create_chat_completion(
        messages=chat_log
    )
    answer = answer["choices"][0]["message"]
    chat_log.append(answer)
    return chat_log

for doc_path in VERSIONS_DIR.glob("**/*.md"):
    doc = TextLoader(doc_path).load()[0]
    if langdetect.detect(doc.page_content) != "fr":
        continue
    splits = text_splitter.split(doc)

    translated_splits = []
    chat_log = None
    for split in splits:
        chat_log = translate(split, chat_log)
        translated_splits.append(chat_log[-1]["content"])
    
    translated_doc = translated_splits.join("\n")

    with open(doc_path, "w") as f:
        f.write(translated_doc)
    