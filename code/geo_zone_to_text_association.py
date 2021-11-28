import tracker_request
import text_corpus
import random

idx = {}


def initialize():
    global idx
    geo_zone_list = tracker_request.get_geo_zone_list()

    if len(geo_zone_list) == 0:
        raise Exception('empty geo zone list')

    text_len = len(text_corpus.contract_text)

    # generate random unique indices, ensure using the min available range
    random_text_indices = random.sample(range(0, text_len),
                                        min(text_len, len(geo_zone_list)))

    for k, geo_zone in enumerate(geo_zone_list):
        # make sure association wraps around in case we have fewer text entries then geo zones
        idx[geo_zone] = random_text_indices[k % text_len]


