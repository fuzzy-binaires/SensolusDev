import requests

url = "https://stickntrack.sensolus.com/rest/api/v2/devices/WQ9ENJ"

querystring = {"apiKey":"36ab8421cb10476b9d8cf46cae0b48a9","_csrf":"a24c8521-aa26-446d-8e65-4f24436bb888%20-H%20%22accept:%20application/json%22"}

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "c2a5e613-80d5-415b-8905-903580310ff9"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)