from tabulate import tabulate
import sys
import csv

order = []
if len(sys.argv) < 2:
    sys.exit("Too few command-lines arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-lines arguments")
if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
try:
    with open(f"{sys.argv[1]}", "r") as file:
        reader = csv.reader(file)
        # Check là Regular hay Sicilian
        for row in reader:
            order.append(row)
        # tabulate chỉ dùng được cho dict
        table = tabulate(order[1:], headers = order[0], tablefmt="grid")
        print(table)
except FileNotFoundError:
    sys.exit("File does not exist")

#cách này lúc đầu tôi dùng dict trong list nhưng không hiệu quả vì phải phân biệt giữa Regular hay Sicilian
    '''
    with open(f"{sys.argv[1]}", "r") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        if 'Regular Pizza' in header:
            for row in reader:
                order.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
        elif 'Sicilian Pizza' in header:
            for row in reader:
                order.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
        table = tabulate.tabulate(order, headers = "keys", tablefmt="grid")
        print(table)
    '''


