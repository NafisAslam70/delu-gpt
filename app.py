from flask import Flask, request, jsonify
from utils.ollama_client import generate_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for frontend)

@app.route("/", methods=["GET"])
def landing():
    return """
    <html>
    <head>
        <title>DELU-GPT</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; max-width: 600px; margin: auto; }
            h1 { color: #2c3e50; }
            input, button { padding: 10px; width: 100%; margin-top: 10px; }
            #responseBox { margin-top: 20px; background: #f4f4f4; padding: 15px; border-radius: 5px; white-space: pre-wrap; }
        </style>
    </head>
    <body>
        <h1>👋 Welcome to DELU-GPT</h1>
        <p>Ask anything below:</p>
        <input type="text" id="userInput" placeholder="Type your question...">
        <button onclick="askGPT()">Ask</button>
        <div id="responseBox"></div>

        <hr>
        <p><strong>Backend API Status:</strong> Online ✅</p>

        <script>
            async function askGPT() {
                const input = document.getElementById("userInput").value;
                const response = await fetch('https://delu-gpt.onrender.com/api/ask', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: input })
                });
                const data = await response.json();
                document.getElementById("responseBox").innerText = data.response || data.error || "No reply.";
            }
        </script>
    </body>
    </html>
    """, 200


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Prompt missing"}), 400

    output = generate_response(prompt)
    return jsonify({"response": output})


@app.route("/api/syllabus", methods=["POST"])
def syllabus():
    data = request.json
    subject = data.get("subject")
    grade = data.get("grade")
    duration = data.get("duration", "3 months")

    prompt = f"You are a teacher. Create a {duration} syllabus for Grade {grade} on the subject '{subject}'. Break it down weekly."
    output = generate_response(prompt)
    return jsonify({"response": output})


@app.route("/api/task-breakdown", methods=["POST"])
def task_breakdown():
    data = request.json
    task_title = data.get("task")

    prompt = f"As a project coordinator, break down the task titled '{task_title}' into 5 weekly sprints with goals and responsible roles."
    output = generate_response(prompt)
    return jsonify({"response": output})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
