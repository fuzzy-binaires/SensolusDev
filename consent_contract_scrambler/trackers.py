from .tracker_request import get_geo_zone_activity
from .text_corpus import modify_text
from .text_corpus import contract_text
from .geo_zone_to_text_association import geo_zone_idx
from os.path import isfile
from datetime import datetime
from .utils import get_max_date
from .utils import concat_pwd
from .printer_control import print_phrase

devices = None


def initialize(start_date):
    print('|∆| :: Querying from date {}'.format(start_date))
    global devices
    file_name = concat_pwd('device_serials.txt')
    if not isfile(file_name):
        raise Exception(' file not found {}'.format(file_name))

    with open(file_name) as serial_file:
        devices = [Tracker(serial_number.rstrip(), start_date) for serial_number in serial_file.readlines()]


class Tracker:
    def __init__(self, serial_number, starting_update_date):
        self.serial_number = serial_number
        self.current_geo_zone = None
        self.previous_geo_zone = None
        self.activity_queue = []
        self.last_update_date = starting_update_date
        self.log_file = open(concat_pwd('generated_text.txt'), 'w+')

    def fill_activity_queue(self):
        today = '{year}-{month}-{day}T00%3A00%3A00Z'.format(year=datetime.now().year,
                                                            month=str(datetime.now().month).zfill(2),
                                                            day=str(datetime.now().day).zfill(2))

        # print(
        #     '-I- query geo zone activity for {} from {} to {}'.format(self.serial_number, self.last_update_date, today))

        activities = get_geo_zone_activity(self.serial_number,
                                                           start_date=self.last_update_date.replace(':', '%3A').replace(
                                                               '+0000', 'Z'),
                                                           end_date=today)

        if len(activities) == 0:
            return

        for activity in activities:
            if 'geozoneId' in activity.keys() and 'exitTime' in activity.keys() and 'geozoneName' in activity.keys():

                self.activity_queue.append({'geozoneId': activity['geozoneId'], 'entryTime': activity['exitTime'],
                                            'geozoneName': activity['geozoneName']})

    def update(self):
        try:
            # if len(self.activity_queue) > 0:
            #     print('|∆| :: Tracker {} queue: {} - query start date: {}'.format(self.serial_number, len(self.activity_queue),
            #                                                        self.last_update_date))
            if len(self.activity_queue) == 0:
                self.fill_activity_queue()

            if len(self.activity_queue) == 0:
                return

            last_activity = self.activity_queue.pop(-1)

            self.current_geo_zone = last_activity['geozoneId']
            geo_zone_name = last_activity['geozoneName']

            self.last_update_date = get_max_date(self.last_update_date, last_activity['entryTime'])

            if self.previous_geo_zone is None or self.previous_geo_zone != self.current_geo_zone:

                idx = geo_zone_idx[geo_zone_name]
                text_from_contract = modify_text(contract_text[idx])

                # print IN CONSOLE the updated text here
                # print(self.serial_number, '@', geo_zone_name, ':', text_from_contract)
                print('=========')
                print(' ')
                print(text_from_contract)
                # send text to a file
                self.log_file.write(text_from_contract)
                print(' ')
                print('=========')
                self.previous_geo_zone = self.current_geo_zone

                # SEND TO printer_control, TO PRINT WITH PHYSICAL THERMAL PRINTER
                print_phrase(text_from_contract)

        except Exception as err:
            # don't kill the program but just ignore
            # this tracker update
            print('|∆| :: Error updating tracker {serial}: {msg}'.format(serial=self.serial_number, msg=err))
            pass
