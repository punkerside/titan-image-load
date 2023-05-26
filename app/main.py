#!/usr/bin/python3

import psutil
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Load Test'

@app.route('/cpu/')
def cpu():
    return 'Web App with CPU!'

@app.route('/mem/')
def mem():
    return 'Web App with MEM!'

app.run(host='0.0.0.0', port=8080)