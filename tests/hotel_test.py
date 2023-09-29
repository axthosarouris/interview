import json

from assertpy import assert_that

from hotel_rating.hotel_rating import Hotel


def should_parse_json_object():
    file = open('../resources/hotel.json')
    data = json.load(file)
    hotel= Hotel.create(data)
    assert_that(hotel.quality).is_equal_to(50)
    assert_that(hotel.pricing_index).is_equal_to(70)