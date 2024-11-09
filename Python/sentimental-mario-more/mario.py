while True:
    try:
        m = int(input("Height: "))
        if 0 < m < 9:
            break
    except ValueError:
        pass
for i in range(m):
    for _ in range(m - i - 1):
        print(" ", end="")
    for _ in range(i + 1):
        print("#", end="")
    print("  ", end="")
    for _ in range(i + 1):
        print("#", end="")
    print("")
