from flask import Blueprint, request, jsonify

from .model import model

# Initialize your Blueprint
api = Blueprint('api', __name__)


@api.route('/generate_answer', methods=['POST'])
def generate_answer():
    data = request.json
    input_text = data['text']
    if(input_text[-1] != '?'):
        input_text += '?'
    model_input = f"Question: {input_text} Answer:"
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
    return jsonify({'response': output_text})
