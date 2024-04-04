from flask import Flask
import os

app = Flask(__name__)

@app.route('/<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8080)
