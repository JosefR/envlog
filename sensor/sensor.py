from enum import Enum

class Sensortype(Enum):
    UNKNOWN = 0
    TEMPERATURE = 1
    PRESSURE = 2 # barometric pressure
    HUMIDITY = 3 
    VELOCITY = 4 # wind velocity

class Sensor:
    def __init__(self, name, sensortype):
        self.name = name
        self.sensortype = sensortype
        self.value = 0.0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sensortype(self):
        return self.sensortype

    def set_sensortype(self, sensortype):
        self.sensortype = sensortype

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val
