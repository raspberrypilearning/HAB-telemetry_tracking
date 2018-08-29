from pytrack import GPS
from time import sleep

gps = GPS()

while True:
    sleep(1)
    data = gps.time,gps.sats,gps.lat,gps.lon,gps.alt
    print("Time: {0}, Satelites: {1}, Latitude: {2}, Londitude: {3}, Altitude: {4}".format(*data))
