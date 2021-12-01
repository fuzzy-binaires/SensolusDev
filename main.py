#!/usr/bin/python
from consent_contract_scrambler import geo_zone_to_text_association
from consent_contract_scrambler import text_corpus
from consent_contract_scrambler import tracker_request
from consent_contract_scrambler import trackers
from consent_contract_scrambler import printer_control

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
update_period = 30  # refresh every n seconds


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
        printer_control.initialize()

        scheduler.enter(update_period, 1, update_devices, (scheduler,))
        scheduler.run()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)