# NLP_Flask_app
Simple Flask application that allows you to send queries to the NLP model

## Installation
In order to use the application you must have a Python distribution installed (application was developed and tested on Python 3.11).  

To setup application on Windows run setup_and_run.bat. The required Python libraries will be installed, the indicated NLP model will be downloaded to the location and the application will be launched on port 8000.  
If this won't work you can do it through PowerShell:
* Installtion of Python libraries
```
pip install -r requirements.txt
```
* Downloading model
```
huggingface-cli download TheBloke/phi-2-GGUF phi-2.Q4_K_M.gguf --local-dir ./app/model
```
* Launching application
```
python -m flask --app app run --port 8000
```

The default model is phi-2.Q4_K_M.gguf and the location for it is ./app/model.  
To change the download location or model, you also need to make this changes in the model.py file

## Usage
After running script or using commands:
* Go to http://localhost:8000/  
* In the first field you can type your prompt to the model (field with header "Wprowadź swoje zapytanie:")
* In the second field you will see answer to your prompt (field with header "Odpowiedź:")
