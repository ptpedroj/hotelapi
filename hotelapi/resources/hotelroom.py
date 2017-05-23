from flask_restful import Resource, reqparse, fields, marshal_with
from hotelapi.models.hotelroomcollection import HotelRoomCollection

class HotelRoom(Resource):
    hoteldb = HotelRoomCollection()

    resource_fields = {
        "city": fields.String,
        "hotelid": fields.String,
        "room": fields.String,
        "price": fields.Float
    }

    parser = reqparse.RequestParser()
    parser.add_argument(
        "cityId",
        type = str,
        required = True,
        help = "This field cannot be left blank. Use a city name, like Bangkok."
    )
    parser.add_argument(
        "sortByPrice",
        type = bool,
        required = False,
        default = False,
        help = "Optional. Sort the list by price (ascending order)."
    )
    parser.add_argument(
        "sortDesc",
        type = bool,
        required = False,
        default = False,
        help = "Optional. If sortByPrice is set to true, then sort in descending order."
    )

    @marshal_with(resource_fields, envelope = "hotelroom")
    def get(self):
        return self._handle_request()


    @marshal_with(resource_fields, envelope = "hotelroom")
    def post(self):
        return self._handle_request()


    def _handle_request(self):
        request_data = HotelRoom.parser.parse_args()
        return HotelRoom.hoteldb.get_hotel_rooms_in_city(
            request_data["cityId"],
            request_data["sortByPrice"],
            request_data["sortDesc"]
        )