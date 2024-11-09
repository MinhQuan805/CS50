def main():
    time = input("What time is it? ")
    result = convert(time)
    # Check if the time is within breakfast hours (7:00 - 8:00)
    if result >= 7 and result <= 8:
        print("breakfast time")
    # Check if the time is within lunch hours (12:00 - 13:00)
    elif result >= 12 and result <= 13:
        print("lunch time")
    # Check if the time is within dinner hours (18:00 - 19:00)
    elif result >= 18 and result <= 19:
        print("dinner time")

def convert(time):
    # Split the input time into hours and minutes
    hours, minutes = time.split(":")
    # Convert the time to a decimal number
    decimal = float(hours) + (float(minutes) / 60)
    return decimal
if __name__ == "__main__":
    main()
