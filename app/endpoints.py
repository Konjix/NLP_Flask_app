from flask import Blueprint, request, jsonify

from .model import model

# Inicjalizacja blueprintu dla api
api = Blueprint('api', __name__)

# Endpoint do generowania odpowiedzi modelu
@api.route('/generate_answer', methods=['POST'])
def generate_answer():
    data = request.json
    input_text = data['text']

    # Dopisanie znaku zapytania na końcu w razie konieczności
    if(input_text[-1] != '?'):
        input_text += '?'

    # Kompozycja zapytania
    model_input = f"Question: {input_text} Answer:"

    # W modelu wykryto sytuacje w których otrzymywana była pusta odpowiedź
    # Pętla powtarza zapytania bez koeczności wykonania kolejnego zapytania post
    while True:
        outputs = model(
            model_input,
            max_tokens=100,
            stop = ["\n", "Question:", "Q"],
            echo = True
        )
        choices = outputs["choices"][0]['text']
        output_text = choices.replace(model_input + " ", "")
        if len(output_text) > 0 and output_text != model_input:
            break
    
    # Zwrócenie odpowiedzi na front
    return jsonify({'response': output_text})
