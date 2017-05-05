from flask import Flask
from webserver import app

# Cheats start here, using the trainer as a "template"


# Health Cheats
@app.route("/api/cheats/health/")
def cheat_health():
    return ""


# Stamina Cheats
@app.route('/api/cheats/stamina/')
def cheat_stamina():
    return ""


# Rupee Cheats
@app.route('/api/cheats/stamina/')
def cheat_rupee():
    return ""


# Mon Cheats
@app.route('/api/cheats/mon/')
def cheat_mon():
    return ""


# Speed Cheats
@app.route('/api/cheats/speed/')
def cheat_speed():
    return ""


# Damage Cheats
@app.route('/api/cheats/damage/')
def cheat_damage():
    return ""


# Weather Cheats
@app.route('/api/cheats/weather/')
def cheat_weather():
    return ""


# Time Cheats
@app.route('/api/cheats/time/')
def cheat_time():
    return ""


# Abilitiy Cheats
@app.route('/api/cheats/abilities/')
def cheat_abilities():
    return ""
