from hotelapi.resources.hotelroom import HotelRoom

import hotelapi.manage as mgr
import hotelapi.models.hotelroom as mhr
import json
import pytest

class TestHotelRoom:
    api_relative_url = "/hotelapi/v1/hotelroom"
    test_cities_with_room_count = {
        "Amsterdam": 6,
        "Ashburn": 13,
        "Bangkok": 7
    }

    @pytest.fixture
    def get_app(self):
        mgr.app.config['TESTING'] = True
        return mgr.app.test_client()


    def test_get_default_response(self):
        app = self.get_app()
        response = app.get(TestHotelRoom.api_relative_url)
        assert json.loads(response.get_data()) == {
            "message": {
                "cityId": "This field cannot be left blank. Use a city name, like Bangkok."
            }
        }


    def test_get_results_for_test_cities(self):
        app = self.get_app()
        for city in TestHotelRoom.test_cities_with_room_count:
            response = app.get(TestHotelRoom.api_relative_url + "?cityId=" + city)
            res_json = json.loads(response.get_data())
            assert len(res_json["hotelroom"]) == TestHotelRoom.test_cities_with_room_count[city]
