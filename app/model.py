from llama_cpp import Llama

# Nazwa modelu
model_name = "app\\model\\phi-2.Q4_K_M.gguf"

# Załadowanie modelu
model = Llama(model_path = model_name, chat_format="llama-2") 
