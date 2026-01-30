from flask import Flask
import os

app = Flask(__name__)

# VULNERABILITY: Hardcoded secret!
AWS_ACCESS_KEY = "AKIA1234567890123456" 

@app.route('/')
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
