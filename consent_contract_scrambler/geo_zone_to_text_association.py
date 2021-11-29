from .tracker_request import get_geo_zone_list
from .text_corpus import contract_text
import random

geo_zone_idx = {}


def initialize():
    global geo_zone_idx
    geo_zone_list = get_geo_zone_list()

    if len(geo_zone_list) == 0:
        raise Exception('empty geo zone list')

    text_len = len(contract_text)

    # generate random unique indices, ensure using the min available range
    random_text_indices = random.sample(range(0, text_len),
                                        min(text_len, len(geo_zone_list)))

    for k, geo_zone in enumerate(geo_zone_list):
        # make sure association wraps around in case we have fewer text entries then geo zones
        geo_zone_idx[geo_zone] = random_text_indices[k % text_len]


