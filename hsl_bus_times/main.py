"""
main.py
Author: @shiimu
Date: 01/12/2021
"""

from flask import Flask, render_template, json
import time
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

# Runs at localhost:5000
if __name__ == "__main__":
    app.run( debug = True )
