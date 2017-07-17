from webserver import app
from time import sleep
from webbrowser import open

def open_page_startup():
    print(f"Opening webpage in {app.config['LAUNCH_OPEN_TIME']}")
    sleep(app.config['LAUNCH_OPEN_TIME'])
    print("Opening page now")
    open(app.config['APP_URL'])