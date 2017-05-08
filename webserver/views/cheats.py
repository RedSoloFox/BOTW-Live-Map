from webserver import app
from webserver.utils.decorators import connect_required
from flask import render_template


@app.route('/cheats/')
@connect_required
def cheats():
    return render_template('cheats.html')