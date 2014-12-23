import serial
import threading
import sensor.sensorcluster
import sensor.sensor

class UsbWde1(sensor.sensorcluster.Sensorcluster):
    def __init__(self, device, baud=9600, sensornames=[]):
        super().__init__()
        self.ser = serial.Serial(port=device, baudrate=baud)
        self.sensor = []
        names = []
        for i in range(0, 8):
            if i >= len(sensornames) or len(sensornames[i]) <= 0:
                names.append('Sensor{}'.format(i))
            else:
                names.append(sensornames[i])
        
        for i in range(0, 8):
            print('add sensor {}'.format(names[i]))
            s_temp = sensor.sensor.Sensor(names[i], sensor.sensor.Sensor.SENSORTYPE_TEMPERATURE)
            s_hum = sensor.sensor.Sensor(names[i], sensor.sensor.Sensor.SENSORTYPE_HUMIDITY)
            self.sensor.append(s_temp)
            self.sensor.append(s_hum)

    def update_sensors(self, data):
        values = data.decode().replace(",",".").split(';')
        for i in range(0, 8):
            if len(values[i + 2]) > 0:
                self.sensor[i*2].set_value(float(values[i + 2]))
            if len(values[i + 10]) > 0:
                self.sensor[i * 2 + 1].set_value(float(values[i + 10]))


    def get_sensordata(self):
        data = ''
        for s in self.sensor:
             data += '{} {}\n'.format(s.get_name(), s.get_value())
        return data

    def get_data(self):
        try:
            line = self.ser.readline()
            if line:
                self.update_sensors(line)
                return line
        except serial.SerialException as e:
            print('something went wrong')
            print(e)
    
    def print_sensordata(self):
        for s in self.sensor:
            value = s.get_value()
            stype = s.get_sensortype()
            if s.is_valid():
                if stype == s.SENSORTYPE_TEMPERATURE:
                    print('{} {}°C'.format(s.get_name(), value))
                elif stype == s.SENSORTYPE_HUMIDITY:
                    print('{} {}%'.format(s.get_name(), value))
                else:
                    print('{} {}.'.format(s.get_name(), value))


