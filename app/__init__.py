
from quart import Quart
appQuart = Quart(__name__)

from flask import Flask

appFlask = Flask(__name__)

from app.views import vFlask
from app.views import vQuart




