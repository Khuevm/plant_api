import json

class PlantInfo:
    def __init__(self, desc, image_link):
        self.desc = desc
        self.image_link = image_link

    def setCareGuide(self, care_guide):
        self.care_guide = care_guide

    def setTitle(self, title):
        self.title = title