import threading
import sensor
import sensor.usbwde1

class Sensorcluster:
    def __init__(self):
        self.running = False

    def print_sensordata(self):
        pass

    def run(self):
        while True:
            print(self.get_data())
            self.print_sensordata()

    def start_thread(self):
        if not self.running:
            threading.Thread(target=self.run).start()
        else:
            print('thread is running already')
 
