# -*- coding: utf-8 -*-
"""
    :author: Nicholas Kobzar
    :repo: https://github.com/n-g-s/simple-app.git
"""

import time

start_time = time.time()


def app_readiness():
    if time.time() - start_time >= 10:
        data = {"ready": True}
        status = 200
        return data, status
    else:
        data = {"ready": False}
        status = 500
        return data, status

