from .tracker_request import get_geo_zone_list
from .text_corpus import contract_text
import random
from .utils import concat_pwd
import os

geo_zone_idx = {}


def initialize():
    global geo_zone_idx
    geo_zone_list = get_geo_zone_list()

    if len(geo_zone_list) == 0:
        raise Exception('empty geo zone list')

    text_len = len(contract_text)

    # check to see if we already have an existing geozone association
    # stored on a file. If this is the case then use it
    association_file = concat_pwd('geo_zone_to_text_association.txt')
    if os.path.isfile(association_file):
        print('-I- using existing association')
        with open(association_file) as f:
            random_text_indices = [int(line) for line in f]
    else:
        # generate random unique indices, ensure using the min available range
        random_text_indices = random.sample(range(0, text_len),
                                            min(text_len, len(geo_zone_list)))

        random_text_indices = [x for x in range(0, text_len)]

        # save indexes to a file
        print('-I- saving existing association into {}'.format(association_file))
        with open(association_file, 'w') as f:
            for idx in random_text_indices:
                f.write('{}\n'.format(idx))

        with open(concat_pwd('human_readable_geo_zone_to_text_association.txt'),'w') as f:
            for idx in random_text_indices:
                sentence = contract_text[idx % len(contract_text)]
                f.write('name: {geozone_name} index {index} sentence: {sentence} \n'.format(geozone_name=geo_zone_list[idx % len(geo_zone_list)],
                                                                                    index=idx, sentence=sentence))


    for k, geo_zone in enumerate(geo_zone_list):
        # make sure association wraps around in case we have fewer text entries then geo zones
        geo_zone_idx[geo_zone] = random_text_indices[k % text_len]


