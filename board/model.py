from transformers import AutoTokenizer, T5ForConditionalGeneration

# Nazwa modelu
model_name = "google/flan-t5-xl"
# Folder do pobrania modelu
model_cache_folder = "D:\\Hugginface_models"

# Załadowanie modelu
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name, cache_dir=model_cache_folder)
