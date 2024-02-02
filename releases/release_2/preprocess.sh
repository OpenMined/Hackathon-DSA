# Re-process pdfs
pip instal nougat-ocr
python ocr-pdf.py

# Add translation for non-english mkdowns
pip install llama-cpp-python langchain langdetect
python translate_documents.py

# Generate retriever inputs
pip install langchain
python gen_retriever_inputs.py
