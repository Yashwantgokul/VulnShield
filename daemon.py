from flask import Flask, request, jsonify, render_template_string
import subprocess

app = Flask(__name__)

# Simple HTML page (frontend)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Command Interface</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; }
    input[type=text] { width: 400px; padding: 8px; }
    button { padding: 8px 16px; }
    #output { margin-top: 20px; white-space: pre-wrap; border: 1px solid #ccc; padding: 10px; background-color: #f9f9f9; }
  </style>
</head>
<body>
  <h1>Command Interface</h1>

  <label for="commandInput">Enter Command:</label>
  <input type="text" id="commandInput" placeholder="Type your command here">
  <button onclick="sendCommand()">Submit</button>

  <div id="output">Output will appear here...</div>

  <script>
    async function sendCommand() {
      const cmd = document.getElementById("commandInput").value;
      if (!cmd) return;

      const outputDiv = document.getElementById("output");
      outputDiv.textContent = `> ${cmd}\\n`;

      try {
        const response = await fetch("/run_command", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ command: cmd })
        });

        const data = await response.json();
        outputDiv.textContent += data.output;
      } catch (err) {
        outputDiv.textContent += "Error: " + err;
      }

      document.getElementById("commandInput").value = "";
    }
  </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/run_command", methods=["POST"])
def run_command():
    data = request.get_json()
    cmd = data.get("command", "")

    if not cmd:
        return jsonify({"output": "No command provided."})

    try:
        # WARNING: This executes commands on your system. Only run trusted commands!
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output_text = result.stdout + result.stderr
    except Exception as e:
        output_text = str(e)

    return jsonify({"output": output_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
