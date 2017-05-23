from hotelapi.common.singleton import Singleton
from hotelapi.models.hotelroom import HotelRoom
from operator import attrgetter

import csv


class HotelRoomCollection(metaclass = Singleton):
    def __init__(self, hotel_room_list = None, data_file_name = None):
        if hotel_room_list is None:
            hotel_room_list = HotelRoomCollection._get_hotel_room_list(data_file_name)

        self.hotel_rooms_by_city = HotelRoomCollection._group_hotel_rooms_by_city(hotel_room_list)



    def get_hotel_rooms_in_city(self, city, isSortedByPrice = False, isSortedAsc = True):
        result = None

        if city in self.hotel_rooms_by_city:
            result = self.hotel_rooms_by_city[city]
            if isSortedByPrice:
                result = sorted(result, key = attrgetter("price"), reverse = not isSortedAsc)

        return result



    @staticmethod
    def _get_hotel_room_list(data_file_name = None):
        if data_file_name is None:
            data_file_name = "./hotelapi/static/hoteldb.csv"

        with open(data_file_name) as data_file:
            return list(map(lambda hr: HotelRoom(hr["CITY"], hr["HOTELID"], hr["ROOM"], hr["PRICE"]), csv.DictReader(data_file)))


    @staticmethod
    def _group_hotel_rooms_by_city(hotel_room_list):
        hoteldb = dict()
        for item in hotel_room_list:
            if item.city in hoteldb:
                hoteldb[item.city].append(item)
            else:
                hoteldb[item.city] = [item]

        return hoteldb