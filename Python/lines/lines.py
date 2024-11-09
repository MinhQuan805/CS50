import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-lines arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-lines arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
try:
    with open(f"{sys.argv[1]}", "r") as file:
        sum = 0
        for line in file:
            line = line.lstrip()
            if line.startswith("#") == True:
                pass
            elif line == "":
                pass
            else:
                sum += 1
        print(sum)
except FileNotFoundError:
    print("File does not exist")


