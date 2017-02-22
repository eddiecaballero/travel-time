import googlemaps
import csv
from datetime import datetime

#Settings
client = googlemaps.Client(key='Add your API Key here')
locationsFile = 'locations.txt'
distancesFile = 'distances.csv'
mode = "driving" #"driving", "walking", "bicycling"
avoid = None #None , "tolls", "highways", "ferries", "indoor"
units = "metric" #"metric", "imperial"
departure_time = datetime.now()
traffic_model = "best_guess" #"best_guess", "pessimistic", "optimistic"

f = open(locationsFile, 'r')
locationsList = map(str.strip, f.readlines())
f.close

f = open(distancesFile, 'wt')
try:
	writer = csv.writer(f)
	writer.writerow(('Origin','Destination', 'Time(' + mode + ')'))
finally:
	f.close()

for origin in locationsList:
	for destination in locationsList:
		if origin != destination:

			matrix = client.distance_matrix(origin, destination, mode=mode, avoid=avoid, units=units, departure_time=departure_time, traffic_model=traffic_model)

			distance =  matrix["rows"][0]["elements"][0]["duration"]["text"]

			f = open(distancesFile, 'a')
			try:
				print origin + " to " + destination + " (" + mode +"): " + distance

				writer = csv.writer(f)
				writer.writerow((origin, destination, distance))
			finally:
				f.close()