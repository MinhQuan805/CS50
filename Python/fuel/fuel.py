
def main():
    X , Y = check()
    remain = (X/Y)*100
    if remain <= 1:
        print("E")
    elif remain >= 99:
        print("F")
    else:
        print(f"{remain:.0f}%")

def check():
    while True:
        energy = input("Fraction: ")
        try:
            X , Y = energy.split("/")
            X = int(X)
            Y = int(Y)
            if Y == 0:
                raise ZeroDivisionError()
            if X > Y:
                raise ValueError()
# Dùng raise để gán lỗi X > Y là Value Error
        except (ValueError, ZeroDivisionError):
            pass
        else:
            return X , Y

main()
