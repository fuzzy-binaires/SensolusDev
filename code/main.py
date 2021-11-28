#!/usr/bin/python
import geo_zone_to_text_association
import text_corpus
import tracker_request
import trackers
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
update_period = 5  # refresh every 5 seconds


def update_devices(sc):
    print('-I- Updating devices')
    for device in trackers.devices:
        device.update()

    scheduler.enter(update_period, 1, update_devices, (sc,))


if __name__ == '__main__':
    try:
        trackers.initialize()
        tracker_request.initialize()
        geo_zone_to_text_association.initialize()
        text_corpus.initialize()

        scheduler.enter(update_period, 1, update_devices, (scheduler,))
        scheduler.run()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)