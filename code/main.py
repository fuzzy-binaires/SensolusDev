#!/usr/bin/python
import geo_zone_to_text_association
import tracker_request
import text_corpus
import tracker

if __name__ == '__main__':
    try:
        tracker_request.initialize()
        geo_zone_to_text_association.initialize()
        trackers = [tracker.Tracker('DLAPWT'), tracker.Tracker('WQ9ENJ')]

        for device in trackers:
            device.update()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)