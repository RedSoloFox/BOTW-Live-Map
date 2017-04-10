from webserver import app
from webserver.utils.decorators import connect_required
from flask import render_template

@app.route("/map/")
@connect_required
def map():
    return render_template("map.html")