from hotelapi.models.hotelroom import HotelRoom
from hotelapi.models.hotelroomcollection import HotelRoomCollection

class TestHotelRoomCollection:
    _test_csv_relative_path = "/../static/hoteldb_test.csv"
    _test_bad_format_csv_relative_path = "/../static/hoteldb_bad_format_test.csv"

    def test_get_hotel_room_list_from_default_csv(self):
        HrList = HotelRoomCollection._get_hotel_room_list()
        assert HrList is not None and \
            len(HrList) > 0 and \
            isinstance(HrList[0], HotelRoom)


    def test_get_hotel_room_list_from_csv(self):
        HrList = HotelRoomCollection._get_hotel_room_list(TestHotelRoomCollection._test_csv_relative_path)
        assert HrList is not None and \
            len(HrList) == 5 and \
            isinstance(HrList[0], HotelRoom)


    def test_fail_get_hotel_room_list_from_missing_csv(self):
        try:
            HrList = HotelRoomCollection._get_hotel_room_list("./does-not-exist.csv")
        except FileNotFoundError:
            assert True
        else:
            assert False


    def test_get_hotel_room_list_from_bad_format_csv(self):
        try:
            HrList = HotelRoomCollection._get_hotel_room_list(
                TestHotelRoomCollection._test_bad_format_csv_relative_path
            )
        except KeyError:
            assert True
        else:
            assert False


    def test_group_hotel_rooms_by_city_single_item(self):
        HrList = [
            HotelRoom("Santiago", 202, "Deluxe", 100.00)
        ]
        HrDict = HotelRoomCollection._group_hotel_rooms_by_city(HrList)

        assert HrDict is not None and \
            len(HrDict) == 1 and \
            len(HrDict[HrList[0].city]) == 1 and \
            HrDict[HrList[0].city][0] is HrList[0]


    def test_group_hotel_rooms_by_city_some_rooms_same_city(self):
        HrList = [
            HotelRoom("Santiago", 101, "Deluxe", 100.00),
            HotelRoom("Santiago", 202, "Deluxe", 100.00),
            HotelRoom("Santiago", 303, "Deluxe", 100.00),
            HotelRoom("Santiago", 404, "Deluxe", 100.00),
            HotelRoom("Santiago", 502, "Deluxe", 100.00)
        ]
        HrDict = HotelRoomCollection._group_hotel_rooms_by_city(HrList)

        assert HrDict is not None and \
            len(HrDict) == 1 and \
            len(HrDict[HrList[0].city]) == 5 and \
            HrDict[HrList[0].city][3] is HrList[3]

    def test_group_hotel_rooms_by_city_some_rooms_diffent_cities(self):
        HrList = [
            HotelRoom("Alexandria", 101, "Deluxe", 100.00),
            HotelRoom("Madrid", 202, "Deluxe", 100.00),
            HotelRoom("Santiago", 303, "Deluxe", 100.00),
            HotelRoom("Tokyo", 404, "Deluxe", 100.00),
            HotelRoom("Washington DC", 502, "Deluxe", 100.00)
        ]
        HrDict = HotelRoomCollection._group_hotel_rooms_by_city(HrList)

        assert HrDict is not None and \
               len(HrDict) == 5 and \
               len(HrDict[HrList[0].city]) == 1 and \
               HrDict[HrList[3].city][0] is HrList[3]


    def test_get_hotel_rooms_in_city(self):
        hrdb = HotelRoomCollection(data_file_name = TestHotelRoomCollection._test_csv_relative_path)
        room_list = hrdb.get_hotel_rooms_in_city("New York")
        assert room_list is not None and \
            len(room_list) == 3 and \
            isinstance(room_list[0], HotelRoom)


    def test_get_hotel_rooms_in_city_missing_city(self):
        hrdb = HotelRoomCollection(data_file_name = TestHotelRoomCollection._test_csv_relative_path)
        assert hrdb.get_hotel_rooms_in_city("Belfast") is None


    def test_get_hotel_rooms_in_city_sort_by_price_asc(self):
        hrdb = HotelRoomCollection(data_file_name = TestHotelRoomCollection._test_csv_relative_path)
        room_list = hrdb.get_hotel_rooms_in_city("New York", isSortedByPrice = True)

        isAscending = True
        for i in range(len(room_list) - 2):
            isAscending = room_list[i].price <= room_list[i + 1].price
            if not isAscending:
                break

        assert isAscending


    def test_get_hotel_rooms_in_city_sort_by_price_desc(self):
        hrdb = HotelRoomCollection(data_file_name = TestHotelRoomCollection._test_csv_relative_path)
        room_list = hrdb.get_hotel_rooms_in_city("New York", isSortedByPrice = True, isSortedDesc = True)

        isDescending = True
        for i in range(len(room_list) - 2):
            isDescending = room_list[i].price >= room_list[i + 1].price
            if not isDescending:
                break

        assert isDescending