import tracker_request
import text_corpus
import random


def associate_geo_zones():
    """
    Random 1:1 association of text elements and geozones
    :return: dictionary associating geo zone names to text section from corpus
    """
    geo_zone_list = tracker_request.get_geo_zone_list()

    if len(geo_zone_list) == 0:
        raise Exception('empty geo zone list')

    text_len = len(text_corpus.contract_text)

    # generate random unique indices, ensure using the min available range
    random_text_indices = random.sample(range(0, text_len),
                                        min(text_len, len(geo_zone_list)))
    geo_zone_to_text_map = {}

    for k, geo_zone in enumerate(geo_zone_list):
        # make sure association wraps around in case we have fewer text entries then geo zones
        geo_zone_to_text_map[geo_zone] = random_text_indices[k % text_len]

    return geo_zone_to_text_map
