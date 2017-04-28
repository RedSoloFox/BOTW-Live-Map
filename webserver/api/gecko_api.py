from webserver import app, bgecko
from webserver.utils.decorators import connect_required
from flask import request, redirect, flash
import json

def convert_to_leaflet(x, y, z):
    x = (12000 + (x*2))
    y = (10000 + (y*2))
    return [x,y, z]

def convert_to_zelda(x,y,z):
    return [x,y,z]

@app.route('/api/coordinates/', methods=["GET", "POST"])
@connect_required
def coordinates():
    try:
        bgecko.coord_address
    except AttributeError:
        bgecko.auto_coord_address()
    if request.method == "GET":
        try:
            coords = bgecko.get_coordinates()
            coords = convert_to_leaflet(coords[0], coords[2], coords[1]) # botwgecko.get_coordinates unpacks to x,z,y
            returnedjson = {"return_status": 0 ,"coordinates":{"x":coords[0], "y":coords[1], "z":coords[2]}}
            return json.dumps(returnedjson)
        except BaseException:
            returnedjson = {"return_status": 1, "coordinates":{"x":"err", "y":"err","z":"err"}}
            return json.dumps(returnedjson)
    # Set coordinates Here


@app.route('/api/connect/', methods=['POST'])
def api_connect():
    if request.form['cord'] == "connect":
        bgecko.connect(request.form['ip'])
        return redirect('/map')
    elif request.form['cord'] == "disconnect":
        bgecko.disconnect()
        flash("Disconnected")
        return redirect('/')
    flash("An error occurred")
    return redirect('/')

@app.route('/api/status/')
@connect_required
def status():
    print(bgecko.is_connected)
    return 'status'

@app.route('/api/cheats/', methods=["GET", "POST"])
@connect_required
def cheats():
    if request.method == "GET":
        return "LIST OF CHEATS"
    return "Cheats"