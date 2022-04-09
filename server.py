from flask import Flask
from flask import request, redirect, url_for, render_template
from base64 import *
import json
from requests import get, post, delete
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        json_file = request.get_json()
        data = json.loads(b64decode(json_file["data"]).decode('utf-8'))
        return redirect(url_for(f'/{data["telemetry"]["firstButton"]["status"]}'), 301)
    except:
        return render_template('start.html')


@app.route('/click')
def click():
    return 'click'


@app.route('/double_click')
def double_click():
    return 'double_click'


@app.route('/long_press')
def long_press():
    return 'long_press'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    '''json_file = get(f'http://localhost:{port}').json()
    data = json.loads(b64decode(json_file["data"]).decode('utf-8'))
    redirect(url_for(f'{data["telemetry"]["firstButton"]["status"]}'), 301)'''
    app.run(host='0.0.0.0', port=port)
