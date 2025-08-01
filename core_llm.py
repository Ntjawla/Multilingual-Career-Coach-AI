
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

llama_model_name = "meta-llama/Llama-3.2-1B-Instruct"
llama_tokenizer = AutoTokenizer.from_pretrained(llama_model_name, use_auth_token=True)
llama_model = AutoModelForCausalLM.from_pretrained(llama_model_name, device_map="auto", torch_dtype=torch.float32)
llama_pipeline = pipeline("text-generation", model=llama_model, tokenizer=llama_tokenizer)

def get_llama_response(prompt):
    wrapped_prompt = f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
    response = llama_pipeline(wrapped_prompt, max_new_tokens=512, do_sample=True)
    return response[0]['generated_text'].split("<|eot_id|>")[-1].strip()
