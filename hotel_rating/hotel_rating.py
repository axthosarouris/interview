import json
from dataclasses import dataclass


@dataclass
class Hotel:

    quality:int  # Quality 1 high, 100 low
    pricing_index:float  # Pricing 1 high, 100 low


def main(hotel_data, user_data, hotel):

    # read the data
    # process