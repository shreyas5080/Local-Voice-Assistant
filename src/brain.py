from llama_cpp import Llama

MODEL_PATH = "model/Llama-3.2-3B-Instruct-Q4_K_M.gguf"

print("🧠 Loading Llama 3B...")
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=4, verbose=False)


def ask_brain(question):
    prompt = f"<|start_header_id|>user<|end_header_id|>\n\n{question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"

    output = llm(prompt, max_tokens=150, stop=["<|eot_id|>"])
    return output['choices'][0]['text'].strip()