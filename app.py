from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/status/<int:number>')
def status(number):
    return f'Code will be {number}', number
