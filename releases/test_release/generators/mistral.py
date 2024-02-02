# from ctransformers import AutoModelForCausalLM, AutoConfig
from transformers import AutoModelForCausalLM, AutoConfig

from transformers import AutoTokenizer
from typing import List, Dict, Optional

TEMPLATE = """
You are a QA assistant that answers questions based only on the context you are given.

Examples:
Q: I am a coding expert. How could I get more info about a Facebook post whose url slug ends with 123456789_123456789? I have a crowdtangle API token (TOKEN). Your output is a bash code snippet.
A: ```bash
curl -L https://api.crowdtangle.com/post/123456789_123456789?token=<CROWDTANGLE_API_TOKEN>
```

Next section will contain the context. You can use it to formulate the answer to the user question.
------------------
{context}
------------------

RULES
- Give an answer ONLY based on the above context and with no prior knowledge.
- If you cannot come up with an answer to the user question, you can answer  like "I do not know the answer to this question".
- Your answers are short, complete and easy to follow. Include code examples if neccessary.
"""


class MistralRAGGenerator:
    def __init__(self, gpu_layers: int = 0):
        self.model = AutoModelForCausalLM.from_pretrained(
            "/gpfsdswork/dataset/HuggingFace_Models/NurtureAI/OpenHermes-2.5-Mistral-7B-16k/",
            # model_file="openhermes-2.5-mistral-7b-16k.Q4_K_M.gguf",
            # model_type="mistral",
            # gpu_layers=gpu_layers,
            # max_new_tokens=4000,
            # context_length=16_000,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            "/gpfsdswork/dataset/HuggingFace_Models/NurtureAI/OpenHermes-2.5-Mistral-7B-16k/"
        )

    def format_prompt(self, messages: List[Dict[str, str]]) -> str:
        return self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        )

    def format_context(self, context: List[str]) -> str:
        context_formatted = []
        for i, c in enumerate(context):
            context_formatted.append(f"CONTEXT {i}\n{c}")

        return "\n\n".join(context_formatted)

    def init_chat_log(
        self, context: List[str], template: Optional[str] = None
    ) -> List[Dict[str, str]]:
        template = template or TEMPLATE
        context = self.format_context(context)
        return [
            {"role": "system", "content": template.format(context=context)},
        ]

    def chat(self, chat_log: List[Dict[str, str]], query: str):
        if query:
            chat_log.append({"role": "user", "content": query})
        if chat_log[-1]["role"] != "user":
            raise ValueError("query required")

        prompt = self.format_prompt(chat_log)
        # output = self.model(prompt, stop=["|im_end|"])
        output = self.model(prompt)
        chat_log.append({"role": "assistant", "content": output})
        return chat_log

    def generate_answer(self, context: str, query: str) -> List[Dict[str, str]]:
        chat_log = self.init_chat_log(context)
        return self.chat(chat_log, query=query)

    def generate_batch(self, contexts: List[List[str]], queries: List[str]) -> List:
        # from tqdm.notebook import tqdm

        res = []
        for context, query in list(zip(contexts, queries)):
            res.append(self.generate_answer(context, query))

        return res
