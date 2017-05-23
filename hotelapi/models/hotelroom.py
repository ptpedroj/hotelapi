class HotelRoom(object):
    def __init__(self, city, hotelid, room, price):
        self.city = city
        self.hotelid = hotelid
        self.room = room
        self.price = float(price)


    def __repr__(self):
        return f"HotelRoom({self.city}, {self.hotelid}, {self.room}, {self.price})"