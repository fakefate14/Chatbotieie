from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/testtest')
def hello2():
    name = request.args.get("name", "World")
    return f'ว่าไงวะสาด!'


if __name__ == "__main__":
    app.run(port=200)