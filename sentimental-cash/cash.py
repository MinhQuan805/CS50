def calculate_quarters(n):
    quarters = 0
    while n >= 25:
        quarters += 1
        n -= 25
    return quarters

def calculate_dimes(n):
    dimes = 0
    while n >= 10:
        dimes += 1
        n -= 10
    return dimes

def calculate_nickels(n):
    nickels = 0
    while n >= 5:
        nickels += 1
        n -= 5
    return nickels

def calculate_pennies(n):
    pennies = 0
    while n > 0:
        pennies += 1
        n -= 1
    return pennies

def main():
    n = -1
    while n < 0:
        try:
            n = round(float(input("Change Owed: ")) * 100)
            if n < 0:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            n = -1

    quarters = calculate_quarters(n)
    n -= quarters * 25

    dimes = calculate_dimes(n)
    n -= dimes * 10

    nickels = calculate_nickels(n)
    n -= nickels * 5

    pennies = calculate_pennies(n)
    n -= pennies * 1

    lap = quarters + dimes + nickels + pennies
    print(lap)

if __name__ == "__main__":
    main()
