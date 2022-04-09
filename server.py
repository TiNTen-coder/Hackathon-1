from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == "GET":
        json_dict = request.get_json()
        print(json_dict)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
