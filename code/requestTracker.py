import requests
import json
import os
from os.path import isfile
from envparse import env


env.read_envfile()
apiKey = env.str('API_KEY')
deviceSerial = env.str('DEVICE_0')


dateObject = {
    "from":{
        "month":10,
        "day":1
    },
    "to":{
        "month":10,
        "day":3
    }
}


########
########


def buildDateStringParam(dates):
    return "&from=2021-"+str(dates["from"]["month"]) + "-" + str(dates["from"]["day"]).zfill(2) + "T00%3A00%3A00Z" + "&to=2021-"+str(dates["to"]["month"]) + "-" + str(dates["to"]["day"]).zfill(2) + "T00%3A00%3A00Z"

def getGeozoneActivity(deviceSerial, dates):
    geozoneData = {"queryType":"geozonevisits/","device":deviceSerial,"timeFrame":buildDateStringParam(dates)}
    thisFlags = "&reevaluate=true" ## NEEDED TO CHECK PAST GEOZONE ACTIVITY
    sendQuery(geozoneData, thisFlags)

def sendQuery(otherParams, flags):
    url = "https://stickntrack.sensolus.com/rest/api/v2/"+ otherParams["queryType"] + otherParams["device"]

    querystring = "apiKey=" + apiKey + otherParams["timeFrame"] + flags +"&_csrf=a24c8521-aa26-446d-8e65-4f24436bb888%20-H%20%22accept:%20application/json%22"
    payload = ""
    headers = {
        'cache-control': "no-cache",
        #'Postman-Token': "c2a5e613-80d5-415b-8905-903580310ff9"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    #print(response.request.url) ## PRINTING THE URL ORIGINALLY CREATED TO SEND THE QUERY
    print("=================")
    ##print(response.text) ## RAW RESPONSE
    ##print("=================")


    data = json.loads(response.text) ## loads RETURNS A DICTIONARY
    ##print('Name of Tracker: ', data['name'])
    
    ## PRINT SOME OF THE GEOLOCATOIN DATA
    for i in range(len(data)):
        print("Visit " + str(i) + " => " + data[i]["geozoneName"] + " @ " + data[i]["entryTime"])


getGeozoneActivity(deviceSerial, dateObject)