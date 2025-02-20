import os
import threading
import subprocess

subprocess.run(["sh", "Terminal.sh"])    # If using sh

def start_server():
    os.system("python base.py")

def start_api():
    os.system("python api.py")

server = threading.Thread(target=start_server)
api = threading.Thread(target=start_api)

server.start()
api.start()
