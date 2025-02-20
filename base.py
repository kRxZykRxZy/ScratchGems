import scratchattach as sa
import time
import random
import string
i = 0
miner = []
for i in range(1):
    def generate_random_letters(length=10):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def write_to_file(filename, content):
        with open(filename, 'w') as file:
            file.write(content) 

    if __name__ == "__main__":
        random_letters = generate_random_letters()
        write_to_file("random_letters.txt", random_letters)
        miner.append(random_letters)


session = sa.login("Username", "Password") #replace with your username and password
cloud = session.connect_cloud("1134723891") #replace with your project id
client = cloud.requests()
log = []
balance = []


@client.request
def ping(): #called when client receives request
    print("Ping request received")
    return "pong" #sends back 'pong' to the Scratch project

@client.request
def gift_recieve(argument1):
    print(f"gift: {argument1}")
    i = 0
    for i in log:
        if log[i] == argument1:
            itemlog = i
            amount = log[i + 1]
            log.remove(argument1)
            log.remove(amount)
            return amount
            return argument1
            balance.replace(itemlog, amount)

@client.request
def gift_send(argument1, argument2):
    print(f"Gift {argument1} to {argument2}")
    log.append(argument2)
    log.append(argument1)
    
@client.request
def mine(argument1):
    print(f"Mining Code: {argument1}")
    i = 0
    for i in miner:
        if miner[i] == argument1:
            return "50"

@client.event
def on_ready():
    print("Request handler is running")

