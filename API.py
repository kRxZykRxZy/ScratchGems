import json
import flask
from flask import *

balances = [] 
with open('scratchgems.json', 'r') as file:
    data = json.load(file)
    balances = data

# API coming soon, still in coding progress. 
import webbrowser
from urllib.parse import urlparse, parse_qs
import pygetwindow as gw
# Get the current URL (this works in specific environments like web automation)
current_url = gw.getActiveWindow().title  # Example method, replace with appropriate one if different
# Parse the URL
parsed_url = urlparse(current_url)
# Extract query parameters
query_params = parse_qs(parsed_url.query)
# Get the 'username' value
username = query_params.get('username', [None])[0]
balance = balances.index(username) + 1
if username:
    print(f"{username}'s balance is {balance}. ")
else:
    print("Username not found in URL")
