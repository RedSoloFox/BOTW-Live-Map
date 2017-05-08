import json

from flask import request

from webserver import app

from webserver.utils.cheats import *


# Cheats start here, using the trainer as a "template"
# Actual cheats will be in the botwgecko, all routes go here

# return_status should be 0 if successful, 1 for errors, document if otherwise


# Health Cheats
@app.route("/api/cheats/health/", methods=['GET', 'POST'])
def cheat_health():
    if request.method == 'GET':
        returnedjson = {"return_status": 0, "health": get_health()}
        return json.dumps(returnedjson)
    # Set Health
    health = request.form['health']
    set_health(health)
    return "200"


# Stamina Cheats
@app.route('/api/cheats/stamina/', methods=['GET', 'POST'])
def cheat_stamina():
    if request.method == 'GET':
        returnedjson = {"return_status": 0, "stamina": "100"}
        return json.dumps(returnedjson)


# Rupee Cheats
@app.route('/api/cheats/rupee/', methods=['GET', 'POST'])
def cheat_rupee():
    if request.method == 'GET':
        returnedjson = {"return_status": 0, "rupees": "999"}
        return json.dumps(returnedjson)


# Mon Cheats
@app.route('/api/cheats/mon/', methods=['GET', 'POST'])
def cheat_mon():
    if request.method == 'GET':
        returnedjson = {"return_status": 0, "coordinates": "999"}
        return json.dumps(returnedjson)


# Speed Cheats
@app.route('/api/cheats/speed/', methods=['POST'])
def cheat_speed():
    returnedjson = {"return_status": 0, "speed": "100"}
    return json.dumps(returnedjson)


# Damage Cheats
@app.route('/api/cheats/damage/', methods=['POST'])
def cheat_damage():
    returnedjson = {"return_status": 0, "damage": "100"}
    return json.dumps(returnedjson)


# Weather Cheats
@app.route('/api/cheats/weather/', methods=['POST'])
def cheat_weather():
    returnedjson = {"return_status": 0, "weather": "clear"}
    return json.dumps(returnedjson)


# Time Cheats
@app.route('/api/cheats/time/', methods=['POST'])
def cheat_time():
    returnedjson = {"return_status": 0, "time": "7:00"}
    return json.dumps(returnedjson)


# Abilitiy Cheats
@app.route('/api/cheats/abilities/', methods=['GET','POST'])
def cheat_abilities():
    returnedjson = {"return_status": 0, "abilities": {"1": "err", "2": "err", "3": "err", "4": "err"}}
    return json.dumps(returnedjson)
