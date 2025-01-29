from flask import Flask, request, jsonify, send_from_directory
import warnings
from flask_cors import CORS
from mail_agent.crew import MailAgent
import webbrowser
import threading
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

FRONTEND_DIR = r"C:\Users\soumy\OneDrive\Desktop\samsung\mail_agent\frontend"

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


def open_browser():
    """Prevents opening the browser twice"""
    if not os.environ.get("WERKZEUG_RUN_MAIN"):  # Prevents duplicate execution
        webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()  # Delay browser opening
    app.run(debug=True, use_reloader=False)  # Disable auto-reloader
