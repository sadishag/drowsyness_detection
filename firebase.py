import requests
import json

# This is just here as a reference.
#state = requests.get(firebase_url)
#firebase_url = "https://blink-8bae2.firebaseio.com/openCV.json"
firebase_url = "https://androidwearheartrate.firebaseio.com/openCV.json"

# set sleeping and status in payload
payload = {"sleeping": "false", "status": "bob"}
headers = {"Content-Type": "application/json"}



# PUT
response = requests.put(firebase_url, data=json.dumps(payload), headers=headers)


