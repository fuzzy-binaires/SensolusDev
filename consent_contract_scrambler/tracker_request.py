# -*- coding: utf-8 -*-

import requests
import json
from os.path import isfile
from envparse import env
from .utils import concat_pwd

apiKey = None


def initialize():
    global apiKey

    # make sure the file exists
    env_file = concat_pwd('.env')
    if isfile(env_file):
        env.read_envfile(env_file)
        apiKey = env.str('API_KEY')
    else:
        raise Exception('Environment file not found')


def get_geo_zone_list():
    """

    :return: a list of unique strings representing the geo zones // RAD!!
    """
    data = send_query('geozones', device_serial=None)
    return [entry['name'] for entry in data]


def build_date_string_param(start_date, end_date):
    """
    :param start_date: ISO8601 date string
    :param end_date: ISO8601 date string
    :return:
    """
    return '&from={start_date}&to={end_date}'.format(start_date=start_date, end_date=end_date)


def get_geo_zone_activity(device_serial, start_date, end_date):
    """
    :param device_serial:
    :param start_date: ISO8601 date string
    :param end_date: ISO8601 date string
    :return: list of activity in date ranges
    """
    geozone_data = {"timeFrame": build_date_string_param(start_date, end_date), "flags": "&reevaluate=true"}
    return send_query('geozonevisits', device_serial, geozone_data)


def send_query(query_type, device_serial, specific_params=None):
    """
    :param query_type: type of query: [ 'geozonevisits', 'geozones' ]
    :param device_serial: serial number of the tracker
    :param specific_params: dictionary with additional parameter specific for the query
    :return: json dictionary with response from the tracker
    """

    url = "https://stickntrack.sensolus.com/rest/api/v2/" + query_type

    # Note that not all commands require the serial
    if device_serial is not None:
        url += "/" + device_serial

    params_string = "apiKey=" + apiKey + \
                    "&_csrf=a24c8521-aa26-446d-8e65-4f24436bb888%20-H%20%22accept:%20application/json%22"

    if specific_params is not None:
        params_string += ''.join(str(x) for x in specific_params.values())

    payload = ""
    headers = {
        'cache-control': "no-cache",
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=params_string)

    data = json.loads(response.text)

    if 'type' in data and data['type'] in ['error', 'unknown']:
        raise Exception('executing command: url: {} data: {} headers: {} params: {} \n\n {}'.format(url, payload,
                                                                                                    headers,
                                                                                                    params_string,
                                                                                                    data['message']))

    return data
