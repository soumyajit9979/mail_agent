from flask import Flask, request, jsonify, send_from_directory
import warnings
from flask_cors import CORS
from mail_agent.crew import MailAgent
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="/")
CORS(app)

@app.route("/draft_mail", methods=["POST"])
def draft_mail():
    try:
        data = request.get_json()
        if "input" not in data:
            return jsonify({"error": "Missing 'input' field"}), 400

        inputs = {"input": data["input"]}
        MailAgent().crew().kickoff(inputs=inputs)

        return jsonify({"message": "Mail drafted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_DIR, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
