# Hackathon-DSA

# Getting the data
```
mkdir -p data
git -C ./data clone https://code.peren.fr/hackathon-2024/retrieval-modules/platform-docs-versions.git
git -C ./data clone https://code.peren.fr/hackathon-2024/retrieval-modules/platform-docs-snapshots.git
```

# Subjects

- Retrieval
    - RAGatouille / ColBERT
    - normal DPR (chromaDB)
    - manual/oldschool methods
- Generation
    - original paper is encoder/decoder (BART)
        - encode all documents + query
        - decode from encoder state 
    - all best models now are decoder-only (GPT/LLama/Mistral/...)
        - put everything in a prompt
- Evaluation
    - metrics
        - faithfulness
        - quality of answers (embedding-based)
        - BLUE/ROUGE, Code quality + reproducibility
        - originality
    - Synthetic dataset
        - https://nlp.stanford.edu/pubs/wang-berant-liang-acl2015.pdf
        - ChatGPT to generate queries/answers?
    - We should get queries/answers from hackathon
        - 10 beforehand 
- Fine-tuning
    - ColBERT/DPR is easy to finetune
    - Mistral is very hard to finetune (in a day)
        - Fine-tuning the prompt is easiest/fastest way to get improvements
     
- UX?
- Involving PySyft?

# Done
- Generation with Mistral (v1 done)

# TODO
- Re-cleaning the data snapshots (Thiago)
    - Langchain has some good document readers
    - PostLight might be an option
    - unstructured?
- send SSH keys (Eelco)
- Evaluation metrics (Teo)
- Synthetic dataset (Teo)
- Semantic search  with DPR (Eelco)

- tune mistral prompt
- Semantic search with [ColBERT](https://github.com/bclavie/RAGatouille)
- Get stuff to work on Jean-Zay
    - Easy deployment for the LLM (vLLM mistral?) 