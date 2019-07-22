#!/usr/bin/env python3

import backend
import web
import threading
from flask import Flask, request


site = Flask(__name__)
@site.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "thres" in request.form:
            backend.PUMP_THRES = float(request.form["thres"]) * 0.1
    return web.get_index()

@site.route("/bootstrap/<path:p>")
def bootstrap(p):
    return web.serve_bootstrap(p)

# Threading stuff has to go at the end of the file because reasons
backend_thread = threading.Thread(target=backend.backend_main)
backend_thread.start()
