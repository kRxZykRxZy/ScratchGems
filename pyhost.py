from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run-python')
def run_python():
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
    return result.stdout

@app.route('/', defaults={'path': ''})  # Default homepage
@app.route('/<path:path>')  # Matches any path
def catch_all(path):
    return open("index.html").read()  # Serves the HTML file

if __name__ == '__main__':
    app.run(debug=True)
