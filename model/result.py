import json
from flask import jsonify
from model.plant import PlantInfo

class Result:
    def __init__(self, id: int, name: str, conf: int, image_link: str):
        self.id = id
        self.name = name
        self.conf = conf
        self.image_link = image_link