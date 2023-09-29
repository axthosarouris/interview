import json
from dataclasses import dataclass


@dataclass
class Hotel:

    quality: int  # Quality 1 high, 100 low
    pricing_index: float  # Pricing 1 high, 100 low

    @staticmethod
    def create(data):
        return Hotel(quality=data["quality"], pricing_index=data["pricing_index"])


def main(hotel_data, user_data, hotel):
    pass
# read the data
# process
