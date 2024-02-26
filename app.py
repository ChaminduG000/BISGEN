from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("abdelhalim/Rec_Business_Names")
model = AutoModelForSeq2SeqLM.from_pretrained("abdelhalim/Rec_Business_Names")

@app.route('/')
def home():
    # Serve the HTML interface
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the request
    data = request.json
    input_text = data['input']

    # Encode the input and generate a response using the model
    input_ids = tokenizer.encode(input_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=50)  # Adjust max_length as needed
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Send the model's response back to the user
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
