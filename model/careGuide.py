import json

class CareGuide:
    def __init__(self, latin, common, tempmin, tempmax, ideallight, toleratedlight, watering):
        self.latin = latin
        self.common = common
        self.tempmin = tempmin
        self.tempmax = tempmax
        self.ideallight = ideallight
        self.toleratedlight = toleratedlight
        self.watering = watering