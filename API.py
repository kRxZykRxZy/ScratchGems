import json
import flask
from flask import *

balances = [] 
with open('scratchgems.json', 'r') as file:
    data = json.load(file)
    balances = data

# API coming soon, still in coding progress. 
import os

app = Flask(__name__)

@app.route('/')
def get_username():
    # Extract 'username' from the query parameters
    username = request.args.get('username')
  

balance = balances.index(username) + 1

if username: 
    with open('html_load.json', 'w') as file:
        json.dump(username, indent = 0)
    with open('balance_html.json', 'w') as file:
        json.dump(balance, indent = 0)
else:
    os.shutdown
if __name__ == '__main__':
    app.run(debug=True)
