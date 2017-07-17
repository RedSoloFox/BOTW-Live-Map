from webserver import app
from webserver.utils.browser_utils import open_page_startup
from threading import Thread
import types, os


# Patch app.run so we can do things at startup
run_old = app.run
def run(self, **kwargs):
    # check if flask has reloaded because of debug, then open if it has finished so it doesn't open twice
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        if app.config["AUTO_LAUNCH_BROWSER"] == True:
            Thread(target=open_page_startup).start()
    run_old(**kwargs)
app.run = types.MethodType(run, app)