import json
from flask import jsonify
from model.plant import PlantInfo

class Result:
    def __init__(self, id: str, name: str, image_link: str):
        self.id = id
        self.name = name
        self.image_link = image_link
        
    def setConf(self, conf: int):
        self.conf = conf