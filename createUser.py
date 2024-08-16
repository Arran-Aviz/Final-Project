import requests
import json

url = "http://10.1.1.134:8000/api/users/"

headers = {
    "Authorization": "Token e3304194e992b8dfe86a39c872b61a1797a5f1e8",
    "Content-Type": "application/json"
}

data = {
    "username": "newuser",         # Replace with the desired username
    "password": "password",
    "first_name": "New",           # Replace with the user's first name
    "last_name": "User",           # Replace with the user's last name
    "email": "newuser@example.com",# Replace with the user's email
    "is_active": True              # Set to True to activate the user
}
