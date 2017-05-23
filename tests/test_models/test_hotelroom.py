from hotelapi.models.hotelroom import HotelRoom

class TestHotelRoom:
    def test_create_hotel_room(self):
        city = "New York"
        hotelid = 1
        room = "Penthouse"
        price = 500.00
        hotel_room = HotelRoom(city, hotelid, room, price)
        assert hotel_room.city == city and \
            hotel_room.hotelid == hotelid and \
            hotel_room.room == room and \
            hotel_room.price == price


    def test_fail_create_hotel_room_invalid_price(self):
        city = "Berlin"
        hotelid = 23
        room = "Double"
        price = "free"
        try:
            hotel_room = HotelRoom(city, hotelid, room, price)
        except ValueError:
            assert True
        else:
            assert False


    def test_hotel_room_repr(self):
        city = "Paris"
        hotel_id = 1
        room = "Single"
        price = 200.00
        hotel_room = HotelRoom(city, hotel_id, room, price)
        assert repr(hotel_room) == f"HotelRoom({city}, {hotel_id}, {room}, {price})"