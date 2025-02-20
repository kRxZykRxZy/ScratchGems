import scratchattach as sa
import time
import random
import string
from local_simple_database import LocalDictDatabase

# Initialize the database to match the second script
LDD = LocalDictDatabase(str_path_database_dir=".", default_value=None)
db = LDD["dict_balances"]
transactions_db = LDD["dict_transactions"]

# Initialize mining and logging
miner = []
log = []

def generate_random_letters(length=10):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Generate a mining code and store it in the database
random_letters = generate_random_letters()
miner.append(random_letters)

def update_balance(username, amount):
    if username in db:
        db[username] += amount
    else:
        db[username] = amount
    LDD.save()  # Save changes to the database

def record_transaction(sender, receiver, amount):
    transactions_db[f"{sender}_to_{receiver}_at_{time.time()}"] = {"from": sender, "to": receiver, "amount": amount}
    LDD.save()

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
        update_balance(argument1, amount)
        return amount
    return "Error: Gift not found"

@client.request
def gift_send(argument1, argument2):
    print(f"Gift {argument1} to {argument2}")
    log.append(argument2)
    log.append(argument1)
    record_transaction("server", argument2, argument1)
    update_balance(argument2, int(argument1))

@client.request
def mine(argument1):
    print(f"Mining Code: {argument1}")
    if argument1 in miner:
        update_balance("miner_user", 50)  # Update balance of miner
        return "50"
    return "Invalid mining code"

@client.event
def on_ready():
    print("Request handler is running")
