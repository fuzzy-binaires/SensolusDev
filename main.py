#!/usr/bin/python
import consent_contract_scrambler.geo_zone_to_text_association
import consent_contract_scrambler.text_corpus
import consent_contract_scrambler.tracker_request
import consent_contract_scrambler.trackers
import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
update_period = 5  # refresh every 5 seconds


def update_devices(sc):
    print('-I- Updating devices')
    for device in consent_contract_scrambler.trackers.devices:
        device.update()

    scheduler.enter(update_period, 1, update_devices, (sc,))


if __name__ == '__main__':
    try:
        consent_contract_scrambler.trackers.initialize()
        consent_contract_scrambler.tracker_request.initialize()
        consent_contract_scrambler.geo_zone_to_text_association.initialize()
        consent_contract_scrambler.text_corpus.initialize()

        scheduler.enter(update_period, 1, update_devices, (scheduler,))
        scheduler.run()

    except Exception as err:
        print('Error in application: {}'.format(err))
        exit(1)