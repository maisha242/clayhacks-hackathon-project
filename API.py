import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
#print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


"""response2 = requests.get("http://api.open-notofy.org/iss-pass.json", params = parameters)
print(response2.status_code)
print(response2.json)
    parameters = {
        "lat": 40.71,
        "lon": -74
    }


jprint2(response2.json())"""


