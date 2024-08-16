import requests
import json

user_id = 2         # ID of the user 
permission_id = 2   # ID from the creation response

url = f"http://10.1.1.134:8000/api/users/users/{user_id}/"
    # use the user id in the URL !!

headers = {
                    # use your api key for this
    "Authorization": "Token e3304194e992b8dfe86a39c872b61a1797a5f1e8",
    "Content-Type": "application/json"
}

    # Update user permissions
data = {
    "permissions": [permission_id]
}
