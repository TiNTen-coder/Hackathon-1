from flask import Flask
from flask import request, redirect, url_for
from base64 import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == "GET":
        json_file = request.get_json()
        data = b64decode(json_file["data"])
        return redirect(url_for(f'{data["first_button"]["status"]}'), 301)

@app.route('/click')
def click():
    return 'click'


@app.route('/double_click')
def double_click():
    return 'double_click'


@app.route('/long_press')
def double_click():
    return 'long_press'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
