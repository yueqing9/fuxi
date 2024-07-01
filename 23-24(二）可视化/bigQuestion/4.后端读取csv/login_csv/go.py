from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'go.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('', filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)