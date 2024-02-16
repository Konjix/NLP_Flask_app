#!/bin/bash

# Step 1: Instalacja bibliotek
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Step 2: Pobranie modelu z Hugging Face
echo "Downloading model to ./app/model directory..."
huggingface-cli download TheBloke/phi-2-GGUF --filename phi-2.Q4_K_M.gguf --local-dir ./app/model

# Step 3: Uruchomienie aplikacji Flask
echo "Starting Flask app on port 8000..."
python -m flask --app app run --port 8000
