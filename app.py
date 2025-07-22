from flask import Flask, request, jsonify
from utils.ollama_client import generate_response
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for frontend)

@app.route("/api/syllabus", methods=["POST"])
def syllabus():
    data = request.json
    subject = data.get("subject")
    grade = data.get("grade")
    duration = data.get("duration", "3 months")

    prompt = f"You are a teacher. Create a {duration} syllabus for Grade {grade} on the subject '{subject}'. Break it down weekly."

    print("Sending prompt to Ollama:", prompt)
    output = generate_response(prompt)
    print("Output received:", output)

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