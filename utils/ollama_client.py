import subprocess

def generate_response(prompt):
    command = ["ollama", "run", "mistral"]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate(input=prompt)

    if error:
        print("Error:", error)

    return output.strip()
