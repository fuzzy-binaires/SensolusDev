from .tracker_request import get_geo_zone_list
from .text_corpus import contract_text
import random
from os.path import isfile

geo_zone_idx = {}


def initialize():
    global geo_zone_idx
    geo_zone_list = get_geo_zone_list()

    if len(geo_zone_list) == 0:
        raise Exception('empty geo zone list')

    text_len = len(contract_text)

    # check to see if we already have an existing geozone association
    # stored on a file. If this is the case then use it
    association_file = 'geo_zone_to_text_association.txt'
    if isfile(association_file):
        print('-I- using existing association')
        with open(association_file) as f:
            random_text_indices = [int(line) for line in f]
    else:
        # generate random unique indices, ensure using the min available range
        random_text_indices = random.sample(range(0, text_len),
                                            min(text_len, len(geo_zone_list)))
        # save indexes to a file
        print('-I- saving existing association into {}'.format(association_file))
        with open(association_file, 'w') as f:
            for idx in random_text_indices:
                f.write('{}\n'.format(idx))

    for k, geo_zone in enumerate(geo_zone_list):
        # make sure association wraps around in case we have fewer text entries then geo zones
        geo_zone_idx[geo_zone] = random_text_indices[k % text_len]


