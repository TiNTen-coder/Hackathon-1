from flask import Flask
from flask import request, redirect, url_for
from flask_cors import CORS
from base64 import *
import json
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def start():
    return app


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=port)
