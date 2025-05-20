from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from GCP CI/CD Pipeline!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)