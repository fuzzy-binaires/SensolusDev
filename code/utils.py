from datetime import datetime


def get_max_date(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%dT%H:%M:%S+0000')
    date2 = datetime.strptime(date_str2, '%Y-%m-%dT%H:%M:%S+0000')

    seconds_1 = (date1 - datetime(1970, 1, 1)).total_seconds()
    seconds_2 = (date2 - datetime(1970, 1, 1)).total_seconds()

    if seconds_1 > seconds_2:
        return date_str1

    return date_str2
