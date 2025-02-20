import os
import threading
import subprocess

subprocess.run(["sh", "Terminal.sh"])  # To install all packages. 

def start_base():
    os.system("python base.py")

def start_api():
    os.system("python api.py")

server = threading.Thread(target=start_server)
api = threading.Thread(target=start_api)

base.start() # Starts base
api.start() # Starts API
