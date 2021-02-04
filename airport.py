import csv
import json

with open('airlines.csv.xls') as file:
    reader = csv.reader(file)
    data = {"names" : []}
    for row in reader:
    	data["names"].append({"Airport_name": row[1], "Repeated" : row[3]})
    	print(data)
airlines.csv
with open("names.json", "w") as f:
	json.dump(data, f)
