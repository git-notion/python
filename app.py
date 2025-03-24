from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

# Serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Run code from frontend
@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data['code']

    try:
        # Run the Python code
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=5)

        if result.returncode == 0:
            output = result.stdout
        else:
            output = result.stderr
    except Exception as e:
        output = str(e)

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
