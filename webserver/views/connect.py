from webserver import app
from flask import render_template

@app.route('/connect/')
def connect():
    return render_template('connect.html')