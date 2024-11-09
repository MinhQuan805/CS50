import random


def main():
    n = get_level()
    score = 0
    for _ in range(10):
        X, Y = generate_integer(n)
        i = 0
        while i < 3:
            try:
                answer = int(input(f"{X} + {Y} = "))
                if X + Y == answer:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                i += 1
        if i == 3:
            print(f"{X} + {Y} = {X + Y} ")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    elif level == 3:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    return X, Y

if __name__ == "__main__":
    main()
