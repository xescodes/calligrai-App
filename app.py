from flask import Flask, render_template, request, jsonify
from dashscope import Generation
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Qwen API
API_KEY = "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"
Generation.api_key = API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    current_text = data.get('text', '')
    tone = data.get('tone', 'Inspirational')
    
    try:
        response = Generation.call(
            model='qwen-max',
            prompt=f"Continue the following text in a {tone} tone:\n{current_text}",
            max_tokens=100
        )
        
        if response.status_code == 200:
            return jsonify({
                'success': True,
                'generated_text': response.output.text
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to generate text'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 