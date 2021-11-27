#!/usr/bin/python
import geo_zone_to_text_association
import tracker_request

if __name__ == '__main__':
    try:
        tracker_request.initialize()

        print('this is the main entry point')
        geo_zone_dict = geo_zone_to_text_association.associate_geo_zones()

        print(geo_zone_dict)

    except Exception as err:
        print(err)
        exit(1)