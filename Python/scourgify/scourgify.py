import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-lines arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-lines arguments")
if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")
try:
    output = []
    with open(sys.argv[1], "r") as info:
        reader = csv.DictReader(info)
        for row in reader:
            last, first = row['name'].split(",")
            output.append({"first": first.strip(), "last": last.strip(), "house" : row["house"]})
    with open(sys.argv[2], "w") as attach:
        writer = csv.DictWriter(attach, fieldnames = ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow(
                {
                    "first": row["first"],
                    "last" : row["last"],
                    "house" : row["house"]
                }
            )


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
