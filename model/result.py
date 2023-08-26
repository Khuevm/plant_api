import json
from flask import jsonify
from model.plant import PlantInfo

class Result:
    def __init__(self, id: int, name: str, conf: int, plant_info: PlantInfo):
        self.id = id
        self.name = name
        self.conf = conf
        self.plant_info = plant_info.__dict__
        