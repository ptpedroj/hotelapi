class HotelRoom(object):
    def __init__(self, city, hotel_id, room, price):
        self.city = city
        self.hotel_id = hotel_id
        self.room = room
        self.price = price


    def __repr__(self):
        return f"HotelRoom({self.city}, {self.hotel_id}, {self.room}, {self.price})"