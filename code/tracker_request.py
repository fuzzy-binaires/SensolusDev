# -*- coding: utf-8 -*-

import requests
import json
from os.path import isfile
from envparse import env

apiKey = None
deviceSerial = None


def initialize():
    global apiKey
    global deviceSerial
    # make sure the file exists
    if isfile('.env'):
        env.read_envfile('.env')
        apiKey = env.str('API_KEY')
        deviceSerial = env.str('DEVICE_0')
    else:
        raise Exception('Environment file not found')


dateObject = {
    "from": {
        "month": 10,
        "day": 1
    },
    "to": {
        "month": 10,
        "day": 3
    }
}


########
########

def get_geo_zone_list():
    """

    :return: a list of unique strings representing the geo zones
    """
    return []


def build_date_string_param(dates):
    return "&from=2021-" + str(dates["from"]["month"]) + "-" + str(dates["from"]["day"]).zfill(
        2) + "T00%3A00%3A00Z" + "&to=2021-" + str(dates["to"]["month"]) + "-" + str(dates["to"]["day"]).zfill(
        2) + "T00%3A00%3A00Z"


def get_geo_zone_activity(device_serial, dates):
    geozone_data = {"queryType": "geozonevisits/", "device": device_serial, "timeFrame": build_date_string_param(dates)}
    this_flags = "&reevaluate=true"  # NEEDED TO CHECK PAST GEO ZONE ACTIVITY
    send_query(geozone_data, this_flags)


def send_query(other_params, flags):
    url = "https://stickntrack.sensolus.com/rest/api/v2/" + other_params["queryType"] + other_params["device"]

    querystring = "apiKey=" + apiKey + other_params[
        "timeFrame"] + flags + "&_csrf=a24c8521-aa26-446d-8e65-4f24436bb888%20-H%20%22accept:%20application/json%22"
    payload = ""
    headers = {
        'cache-control': "no-cache",
        # 'Postman-Token': "c2a5e613-80d5-415b-8905-903580310ff9"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # print(response.request.url) ## PRINTING THE URL ORIGINALLY CREATED TO SEND THE QUERY
    print("=================")
    # print(response.text) ## RAW RESPONSE
    # print("=================")

    data = json.loads(response.text)  # loads RETURNS A DICTIONARY
    # print('Name of Tracker: ', data['name'])

    # PRINT SOME OF THE GEO LOCATION DATA
    for i in range(len(data)):
        print("Visit " + str(i) + " => " + data[i]["geozoneName"] + " @ " + data[i]["entryTime"])

