

import requests
import json
import csv

url = 'https://covid19.saglik.gov.tr/covid19api?getir=liste'

r = requests.get(url)

data = r.json()
print(data)

covidDataset = data

# now we will open a file for writing
data_file = open('covid.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in covidDataset:
    if count == 0:
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

data_file.close()
