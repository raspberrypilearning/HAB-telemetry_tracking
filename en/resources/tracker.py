from pytrack import GPS,PITS_LED
from time import sleep
from datetime import datetime

gps = GPS()
status = PITS_LED()

filename = datetime.now().strftime("/home/pi/%Y-%m-%d-%H:%M:%S.csv") 

while True:
    sleep(1)
    data = [gps.time,gps.sats,gps.lat,gps.lon,gps.alt]
    if gps.sats<3:
        status.gps_lock_status(False)
    else:
        status.gps_lock_status(True)
        print("Time: {}, Satelites: {}, Latitude: {}, Londitude: {}, Altitude: {}".format(*data))
        out = ",".join(str(i) for i in data)+"\n"
        with open(filename,"a") as f:
            f.write(out)



