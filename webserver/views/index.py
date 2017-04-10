from webserver import app, bgecko
from flask import redirect

@app.route('/', methods=["GET"])
def index():
    if bgecko.is_connected:
        return redirect('/map/')
    return redirect('/connect/')