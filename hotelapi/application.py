from flask import Flask
from flask_restful import Api

from hotelapi.resources.hotelroom import HotelRoom

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    api = Api(app)
    api.add_resource(HotelRoom, "/hotelapi/v1/hotelroom")

    return app