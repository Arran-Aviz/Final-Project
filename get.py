import requests
import json

url = "http://10.1.1.134:8000/api/dcim/devices/"
	#use your ip address here

payload = {}
files={}
headers = {
  'Authorization': 'Token e3304194e992b8dfe86a39c872b61a1797a5f1e8'
}		# generate a token to use (see netbox docs to make one)

response = requests.request("GET", url, headers=headers, data=payload, files=files)
response_json = response.json()
devices = response_json.get('results', [])

for device in devices:
    device_name = device.get('name')

pretty_json = json.dumps(response_json, indent=4)
print(pretty_json)
