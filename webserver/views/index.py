from webserver import app, bgecko
from flask import render_template, request, redirect, flash

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')