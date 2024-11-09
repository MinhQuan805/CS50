def main():
    text = input("Input: ")
    text = shorten(text)
    print("Output:", text)



def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for c in vowels:
        word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()
