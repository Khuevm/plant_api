import json

class PlantInfo:
    def __init__(self, title, desc, image_link = ""):
        self.title = title
        self.desc = desc
        self.image_link = image_link

    def __init__(self, title, desc, image_link = "", care_guide):
        self.title = title
        self.desc = desc
        self.image_link = image_link
        self.careGuide = care_guide.__dict__
