#!/usr/bin/python
import geo_zone_to_text_association
import tracker_request
import tracker
from os.path import isfile
import sched
import time

trackers = None
scheduler = sched.scheduler(time.time, time.sleep)
update_period = 5  # refresh every 5 seconds


def initialize_devices():
    global trackers
    file_name = 'device_serials.txt'
    if not isfile(file_name):
        raise Exception(' file not found {}'.format(file_name))

    with open(file_name) as serial_file:
        trackers = [tracker.Tracker(serial_number.rstrip()) for serial_number in serial_file.readlines()]


def update_devices(sc):
    print('-I- Updating devices')
    for device in trackers:
        device.update()

    scheduler.enter(update_period, 1, update_devices, (sc,))


if __name__ == '__main__':
    try:
        initialize_devices()
        tracker_request.initialize()
        geo_zone_to_text_association.initialize()

        scheduler.enter(update_period, 1, update_devices, (scheduler,))
        scheduler.run()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)