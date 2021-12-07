#!/usr/bin/python
from consent_contract_scrambler import geo_zone_to_text_association
from consent_contract_scrambler import text_corpus
from consent_contract_scrambler import tracker_request
from consent_contract_scrambler import trackers
from consent_contract_scrambler import printer_control
from datetime import datetime
import argparse

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
update_period = 15  # refresh every n seconds


def update_devices(sc):
    print('-I- Updating devices')

    for device in trackers.devices:
        device.update()

    scheduler.enter(update_period, 1, update_devices, (sc,))


if __name__ == '__main__':
    try:
        today = '{year}-{month}-{day}T00:00:00+0000'.format(year=datetime.now().year,
                                                            month=str(datetime.now().month).zfill(2),
                                                            day=str(datetime.now().day).zfill(2))

        parser = argparse.ArgumentParser(description='Query sensor network from initial date and generate text to print')
        parser.add_argument('start_date', metavar='d', nargs='?', type=str, default=today,
                            help='The start date to query for geo-zone updates. Format yy-mm-ddT00:00:00+0000')
        args = parser.parse_args()

        trackers.initialize(args.start_date)
        tracker_request.initialize()
        geo_zone_to_text_association.initialize()
        text_corpus.initialize()
        printer_control.initialize()

        scheduler.enter(update_period, 1, update_devices, (scheduler,))
        scheduler.run()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)
