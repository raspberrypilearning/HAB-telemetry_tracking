import folium
import csv

with open("2018-08-29-10:47:35.csv","r") as f:
    reader = csv.reader(f)
    results = {}

    for row in reader:
        key = row[0]
        if key in results:
            pass
        results[key] = row[2:4]




points = []
for i in list(results.keys())[1:]:
    point = float(results[i][0]),float(results[i][1])
    points.append(point)
m = folium.Map(location=[float(results[i][0]),float(results[i][1])])
folium.PolyLine(points[1:]).add_to(m)
m.save('wsmap1.html')
