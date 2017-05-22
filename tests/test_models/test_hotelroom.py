from hotelapi.models.hotelroom import HotelRoom

class TestHotelRoom:
    def test_create_hotel_room(self):
        city = "New York"
        hotel_id = 1
        room = "Penthouse"
        price = "500.00"
        hotel_room = HotelRoom(city, hotel_id, room, price)
        assert hotel_room.city == city and \
            hotel_room.hotel_id == hotel_id and \
            hotel_room.room == room and \
            hotel_room.price == price


    def test_hotel_room_repr(self):
        city = "Paris"
        hotel_id = 1
        room = "Single"
        price = "200.00"
        hotel_room = HotelRoom(city, hotel_id, room, price)
        assert repr(hotel_room) == f"HotelRoom({city}, {hotel_id}, {room}, {price})"
