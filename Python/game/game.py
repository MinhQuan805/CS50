from random import randint
while True:
    try:
        level =  int(input("Level: "))
        if level > 0:
            break

    except ValueError:
        pass
num = randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= level:
            if guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            elif guess == num:
                print("Just right!")
                break
    except ValueError:
        pass
