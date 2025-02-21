import scratchattach as sa
import time
import random
import string

# Initialize mining and logging
miner = []
log = []

def generate_random_letters(length=10):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Generate a mining code
random_letters = generate_random_letters()
miner.append(random_letters)

session = sa.login("Username", "Password")  # Replace with your credentials
cloud = session.connect_cloud("1134723891")  # Replace with your project ID
client = cloud.requests()

@client.request
def ping():
    print("Ping request received")
    return "pong"

@client.request
def gift_receive(argument1):
    print(f"Gift received request: {argument1}")
    if argument1 in log:
        amount = log.pop(log.index(argument1) + 1)
        log.remove(argument1)
        return amount

@client.request
def gift_send(argument1, argument2):
    print(f"Gift {argument1} to {argument2}")
    log.append(argument2)
    log.append(argument1)

@client.request
def mine(argument1):
    print(f"Mining Code: {argument1}")
    if argument1 in miner:
        return "100"

@client.event
def on_ready():
    print("Request handler is running")
