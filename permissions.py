import requests
import json

url = "http://10.1.1.134:8000/api/users/permissions/"
	#use your ip address here

headers = {
    "Authorization": "Token e3304194e992b8dfe86a39c872b61a1797a5f1e8",
    # generate a token to use (see netbox docs to make one)
    "Content-Type": "application/json"
}

    # create the id arrays of the actual ids of the information!
site_id = 2
device_id = [3, 4, 5, 6]
cable_id = [2,3,4,5,6,7]
rack_id = 2
devicetype_id = [3, 4]

    #example using Celestica
data = {
    "name": "CelesticaPermissions",
    "actions": ["view"],
    "object_types": [
        "dcim.site",
        "dcim.device",
        "dcim.cable",
        "dcim.rack",
        "dcim.devicetype"
    ],
    "constraints":[
        {"content_type": "dcim.site", "object_id": site_id},
        {"content_type": "dcim.device", "object_ids": device_id},
        {"content_type": "dcim.cable", "object_ids": cable_id},
        {"content_type": "dcim.rack", "object_id": rack_id },
        {"content_type": "dcim.devicetype", "object_ids": devicetype_id}
        # allows the Celestica Viewer to only see these DCIM components
    ]
}
