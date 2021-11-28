import tracker_request
import text_corpus
import geo_zone_to_text_association


class Tracker:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.current_geo_zone = None
        self.previous_geo_zone = None
        pass

    def update(self):
        try:
            activity = tracker_request.get_geo_zone_activity(self.serial_number,tracker_request.dateObject)
            if len(activity) == 0:
                return
            last_activity = activity[-1]
            geo_zone_name = ''
            if 'geozoneId' in last_activity:
                self.current_geo_zone = last_activity['geozoneId']
                geo_zone_name = last_activity['geozoneName']

            if self.previous_geo_zone is None or self.previous_geo_zone != self.current_geo_zone:
                # print the updated text here
                idx = geo_zone_to_text_association.idx[geo_zone_name]
                print(self.serial_number, '@', geo_zone_name, ':', text_corpus.modify_text(text_corpus.contract_text[idx]))
                self.previous_geo_zone = self.current_geo_zone

        except Exception as err:
            # don't kill the program but just ignore
            # this tracker update
            print('Error updating tracker {serial}: {msg}'.format(serial=self.serial_number, msg=err))
            pass
