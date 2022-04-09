from flask import Flask
from flask import request
from base64 import *

app = Flask(__name__)


@app.route('/', methods=['POST'])
def start():
    if request.method == "POST":
        data = request.get_json()
    return data


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
