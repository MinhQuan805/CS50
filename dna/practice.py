import csv

with open("databases/large.csv") as file:
    reader = csv.DictReader(file)
    header = reader.fieldnames
    print(header[0])
