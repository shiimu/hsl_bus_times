from flask import Flask, render_template, json, jsonify
import time
import requests
from requests.models import Response

app = Flask(__name__)


@app.route("/")
def index():
    from query_stop_times import queryApi
    queryApi('HSL:1472128')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
