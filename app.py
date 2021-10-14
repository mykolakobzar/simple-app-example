# -*- coding: utf-8 -*-
"""
    :author: Nicholas Kobzar
    :repo: https://github.com/n-g-s/simple-app.git
"""

from timer import timer
from flask import Flask, Response, jsonify, make_response
from prometheus_client import Counter
from prometheus_client import generate_latest


app = Flask(__name__)
keda_metric = Counter('keda', 'Application view count')
MESSAGE = "Hello world"


@app.route('/')
def index():
    keda_metric.inc()
    return Response(MESSAGE, mimetype="text/plain")


@app.route('/status/alive')
def liveness():
    response = Response(status=200)
    return response


@app.route('/status/ready')
def readiness():
    data = timer.app_readiness()
    return make_response(jsonify(data[0]), data[1])

@app.route('/metrics')
def metrics():
    return generate_latest()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
