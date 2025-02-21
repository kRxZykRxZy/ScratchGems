import json
import flask
from flask import *

with open(ScratchGems.json, 'r' ) as file:
    data = json.read(file)

# API coming soon, still in coding progress
