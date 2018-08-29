from pytrack import GPS
from time import sleep
from datetime import datetime

gps = GPS()

filename = datetime.now().strftime("/home/pi/%Y-%m-%d-%H:%M:%S.csv") 
with open(filename,"w") as f:
    f.write("Time,Satelites,Latitude,Londitude,Altitude\n")

while gps.fix!=1:
   pass

while True:
    sleep(1)
    data = [gps.time,gps.sats,gps.lat,gps.lon,gps.alt]
    print("Time: {}, Satelites: {}, Latitude: {}, Londitude: {}, Altitude: {}".format(*data))
    out = ",".join(str(i) for i in data)+"\n"
    with open(filename,"a") as f:
        f.write(out)

