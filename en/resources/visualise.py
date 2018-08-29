import folium
import csv

from os import listdir
log_files = listdir("/home/pi/")
csv_files = [filename[:-4] for filename in log_files if filename.endswith(".csv")]
html_files = [filename[:-5] for filename in log_files if filename.endswith(".html")]

for csv_file in csv_files:
    if csv_file in html_files:
        pass
    else:
        with open(csv_file+".csv","r") as f:
            reader = csv.reader(f)
            results = {}


            for row in reader:
                key = row[0]
                if key in results:
                    pass
                results[key] = row[2:4]

        points = []

        key_list= list(results.keys())[1:]
        key_list.sort()

        if len(key_list) > 0:

            for i in key_list:
                point = float(results[i][0]),float(results[i][1])
                points.append(point)

            m = folium.Map(location=points[0])

            folium.PolyLine(points[1:]).add_to(m)
            m.save(csv_file+'.html')
