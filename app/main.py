#!/usr/bin/python3

import multiprocessing
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Load Test'

@app.route('/cpu/')
def cpu():
    active = multiprocessing.active_children()
    for child in active:
        child.kill()
    process = multiprocessing.Process(target=task)
    process.start()
    return 'Web App with CPU!'
def task():
    timer = 0
    while 1:
        # sum = timer ** timer
        sum = 5734 ** 6397
        print(sum)
        timer += 1
        time.sleep(1/1000)

@app.route('/reset/')
def reset():
    active = multiprocessing.active_children()
    for child in active:
        child.kill()
    return 'Web App with CPU!'

app.run(host='0.0.0.0', port=8080)