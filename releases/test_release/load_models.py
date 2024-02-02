import os
import pathlib

models_dir = pathlib.Path('./models')
models_dir.mkdir(exist_ok=True)
os.environ['HF_HOME'] = str(models_dir)

# NOTE should be imported after setting HF_HOME
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoTokenizer, AutoModel
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForMaskedLM.from_pretrained("bert-base-uncased")

# Preload mbart translation
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

tokenizer = AutoTokenizer.from_pretrained("colbert-ir/colbertv2.0")
model = AutoModel.from_pretrained("colbert-ir/colbertv2.0")

# Preload mistral + tokenizer
AutoTokenizer.from_pretrained("NurtureAI/OpenHermes-2.5-Mistral-7B-16k")
# AutoModelForCausalLM.from_pretrained(
#     "TheBloke/OpenHermes-2.5-Mistral-7B-16k-GGUF",
#     model_file="openhermes-2.5-mistral-7b-16k.Q4_K_M.gguf",
#     model_type="mistral",
#     gpu_layers=0,
#     max_new_tokens=4000,
#     context_length=16_000,
# )