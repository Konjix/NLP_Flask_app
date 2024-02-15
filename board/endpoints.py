from flask import Blueprint, request, jsonify

from .model import model, tokenizer

# Initialize your Blueprint
api = Blueprint('api', __name__)


@api.route('/generate_answer', methods=['POST'])
def generate_answer():
    data = request.json
    input_text = data['text']
    # Assuming the tokenizer and model are accessible here
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_new_tokens=50)
    edited_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'response': edited_text})
