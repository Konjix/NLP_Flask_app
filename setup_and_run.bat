@echo off
REM Step 1: Pobranie modelu z Hugging Face
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Step 2: Pobranie modelu z Hugging Face
echo Downloading model to .\app\model directory...
huggingface-cli download TheBloke/phi-2-GGUF --filename phi-2.Q4_K_M.gguf --local-dir .\app\model

REM Step 3: Uruchomienie aplikacji Flask
echo Starting Flask app on port 8000...
set FLASK_APP=app
flask run --port 8000