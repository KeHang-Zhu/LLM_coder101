from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_chatbot_response(user_input)
    return jsonify(response)

def get_chatbot_response(user_input):
    # Replace 'your_api_key_here' with your actual OpenAI API key
    api_key = ''
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': user_input}]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    print(response.json())  # Add this line to print the response
    return response.json()


@app.route('/')
def home():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
