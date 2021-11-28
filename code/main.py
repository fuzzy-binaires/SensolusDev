#!/usr/bin/python
import geo_zone_to_text_association
import tracker_request
import tracker
import sched, time

trackers = [tracker.Tracker('DLAPWT'), tracker.Tracker('WQ9ENJ')]
scheduler = sched.scheduler(time.time, time.sleep)
update_period = 5  # refresh every 5 seconds

def update_devices(sc):
    print('-I- Updating devices')
    for device in trackers:
        device.update()

    scheduler.enter(update_period, 1, update_devices, (sc,))

if __name__ == '__main__':
    try:
        tracker_request.initialize()
        geo_zone_to_text_association.initialize()

        scheduler.enter(update_period, 1, update_devices, (scheduler,))
        scheduler.run()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)