#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.mail_agent.crew import MailAgent

app = Flask(__name__)
CORS(app)

@app.route('/send-mail', methods=['POST'])
def send_mail():
    try:
        data = request.get_json()
        user_input = data.get('input')  # Extract input from frontend

        if not user_input:
            return jsonify({'error': 'Input is required'}), 400

        response = MailAgent().crew().kickoff(inputs={'input': user_input})  # Run CrewAI agent
        
        # Convert CrewOutput to a JSON-serializable format
        response_data = str(response)  # Convert to string (or extract relevant data)

        return jsonify({'message': 'Mail drafted successfully', 'response': response_data})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
