from pytrack import GPS
from time import sleep

gps = GPS()

while True:
    sleep(1)
    print(gps.position().time)
