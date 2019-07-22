import backend
from flask import Response

def get_index():
    index = None
    with open("index.html") as index_f:
        index = index_f.read().replace("__SLIDER_VALUE__", str(int(10*backend.PUMP_THRES)))
        index = index.replace("__MOIST_DATA__", str(backend.moist_data))
        index = index.replace("__PUMP_DATA__", str(backend.pump_data))
        index = index.replace("__TIMES__", str(backend.times))

    return index

def serve_bootstrap(path):
    v = None
    mt = "text/html"
    try:
        with open("bootstrap/"+path) as f:
            v = f.read()
            if path[-3:] == ".js":
                mt = "text/javascript"
            elif path[-3:] == "css":
                mt = "text/css"
        return Response(v, mimetype=mt)
    except FileNotFoundError:
        return "File not found", 404
