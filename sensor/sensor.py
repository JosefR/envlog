import time

class Sensor:
    SENSORTYPE_UNKNOWN = 0
    SENSORTYPE_TEMPERATURE = 1
    SENSORTYPE_PRESSURE = 2 # barometric pressure
    SENSORTYPE_HUMIDITY = 3 
    SENSORTYPE_VELOCITY = 4 # wind velocity

    def __init__(self, name, sensortype):
        self.name = name
        self.sensortype = sensortype
        self.value = -99.9 # TODO a better way to mark invalid data
        self.last_update = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sensortype(self):
        return self.sensortype

    def set_sensortype(self, sensortype):
        self.sensortype = sensortype

    def is_valid(self):
        # invalid if older than 15 min
        ts = time.time()
        if (ts - self.last_update) > 900:
            return False
        return True

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val
        self.last_update = time.time()

