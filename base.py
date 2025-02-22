import scratchattach as sa
import time
import random
import string
import json
import subprocess

# Specify the path to your shell script
script_path = './Terminal.sh'

# Run the shell script
subprocess.run(['sh', script_path])


# Open and read the JSON file
with open('scratchgems.json', 'r') as file:
    data = json.load(file)
    
    people = data

print(data)  # Prints the JSON content as a dictionary



 # Initialize mining and logging
miner = []
log = []

def generate_random_letters(length=10):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Generate a mining code
random_letters = generate_random_letters()
miner.append(random_letters)

session = sa.login("USERNAME", "PASSWORD")  # Replace with your credentials
cloud = session.connect_cloud("1134723891")  # Replace with your project ID
client = cloud.requests()

with open('scratchgems.json', 'w') as file:
    json.dump(people, indent = 0)

@client.request
def ping():
    print("Ping request received")
    return "pong"

@client.request
def gift_receive(argument1):
    print(f"Gift received request: {argument1}")
    return people[people.index(argument1) + 1]
    with open('scratchgems.json', 'w') as file:
        json.dump(people, indent = 0)


@client.request
def gift_send(argument1, argument2, argument3):
    print(f"Gift {argument1} to {argument2}")
    if argument2 in people:
        bal = people.index(argument3) + 1
        people[bal] = people[bal] - argument1
        balance1 = people.index(argument2) + 1
        people[balance1] = people[balance1] + argument1
        with open('scratchgems.json', 'w') as file:
            json.dump(people, indent = 0)
    
@client.request
def mine(argument1, argument2):
    print(f"Mining Code: {argument1}")
    if argument1 in miner:
        client.send(message)
        return "100"
        numb = people.index(argument2)
        people[numb + 1] = 100 + people[numb + 1]
        with open('scratchgems.json', 'w') as file:
            json.dump(people, indent = 0)

@client.request
def new(argument1):
    print(f"New: {argument1}")
    if argument1 in people:
        true = false
    elif 10 == 10:
        people.append(argument1)
        people.append("100")
        return "new"
        with open('scratchgems.json', 'w') as file:
            json.dump(people, indent = 0)
    
@client.event
def on_ready():
    print("Request handler is running")
