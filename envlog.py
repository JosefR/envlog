#!/usr/bin/env python3

import argparse
import time
import sensor.usbwde1
import viewer.viewer

def main():
    parser = argparse.ArgumentParser(description='Log weather data.')
    parser.add_argument('sensorcluster', metavar='Sensorcluster', type=str, nargs='+',
        help='sensor cluster and names; e.g.: usbwde1:/dev/ttyUSB0:Indoors1,Indoors2,Outdoors1,A,B,C,D,E')
    args = parser.parse_args()

    print(args.sensorcluster)

    sc = []
    for cluster in args.sensorcluster:
        d = cluster.split(':')
        device = d[0]
        print('o')
        print(cluster)
        print(device)

        if device == 'usbwde1':
            devpath = d[1]
            snames = d[2].split(',')
            print('devpath {}', devpath)
            s = sensor.usbwde1.UsbWde1(device=devpath, sensornames=snames)
            sc.append(s)
        else:
            print('unknown sensorcluster')

    # start the threads
    for cluster in sc:
        cluster.start_thread()
        print('initlialized sensor cluster')

    # run webserver
    v = viewer.viewer.Viewer(port=8000)
    v.start()

    #t = viewer.viewer.TestThread()
    #t.start()

    # a really stupid way of reading out the current sensor data by polling
    cnt = 0
    while 1:
        time.sleep(10)
        cnt += 1
        f = open('/tmp/sensordata', 'w')
        for cluster in sc:
            f.write(cluster.get_sensordata())
        print("envlog ...")


if __name__ == '__main__':
    main()
