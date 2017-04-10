from flask import Flask
from botwgecko import BOTWGecko

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

#BOTWGecko init
bgecko = BOTWGecko()

# Import the other sections
import webserver.utils
import webserver.views
import webserver.api

if __name__ == '__main__':
    app.run()