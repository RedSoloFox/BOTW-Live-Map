from webserver import app
from flask import render_template
from webserver.utils.decorators import connect_required

@connect_required
@app.route('/settings/')
def settings():
    return render_template("settings.html")