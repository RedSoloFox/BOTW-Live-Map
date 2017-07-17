# Flask Config #
SECRET_KEY = "secret key which should be changed"
DEBUG = True

'''
# Flask_SQLAlchemy #
# SQLAlchemy has not been implemented as of yet, and as such the config has been commented out
SQLALCHEMY_DATABASE_URI = ''
SQLALCHEMY_TRACK_MODIFICATIONS = False
'''

# BOTW-LM CONFIG #
AUTO_LAUNCH_BROWSER = False
APP_URL = "http://localhost:5000"
LAUNCH_OPEN_TIME = 5

# This should be used only if your Wii U is setup with a static IP, otherwise it won't connect if it changes
WIIU_IP = "192.168.X.X"
WIIU_AUTO_CONNECT = False