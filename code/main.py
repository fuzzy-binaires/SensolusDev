#!/usr/bin/python
import geo_zone_to_text_association
import tracker_request
import text_corpus

if __name__ == '__main__':
    try:
        tracker_request.initialize()

        geo_zone_dict = geo_zone_to_text_association.associate_geo_zones()

        print(geo_zone_dict)

        for zone in geo_zone_dict:
            idx = geo_zone_dict[zone]
            print(zone, ':', text_corpus.modify_text( text_corpus.contract_text[idx] ) )

        data = tracker_request.get_geo_zone_activity(tracker_request.deviceSerial, tracker_request.dateObject)

        for i in range(len(data)):
            print("Visit " + str(i) + " => " + data[i]["geozoneName"] + " @ " + data[i]["entryTime"])

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)