import threading
import sensor
import sensor.usbwde1

class Sensorcluster:
    def __init__(self):
        pass

    def print_sensordata(self):
        pass

    def get_sensordata(self):
        pass

    def run(self):
        while True:
            print(self.get_data())
            self.print_sensordata()

    def start_thread(self):
        threading.Thread(target=self.run).start()
 
