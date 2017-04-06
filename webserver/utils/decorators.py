from functools import wraps
from webserver import bgecko
from flask import redirect, flash


def connect_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if bgecko.is_connected:
            return func(*args, **kwargs)
        flash("Please Connect")
        return redirect('/')

    return decorated_view