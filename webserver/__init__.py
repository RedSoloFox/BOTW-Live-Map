from flask import Flask
from botwgecko import BOTWGecko

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

# create object for later reassignment so it can be shared
bgecko = BOTWGecko()

'''
# for debug, will freeze on re-init by the debugger
if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
    bgecko = BOTWGecko(app.config["WIIUIP"])
else:
    bgecko = None
'''

import webserver.utils
import webserver.views
import webserver.api