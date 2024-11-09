import math

def coleman(text):
    l = 0  # số lượng chữ cái
    s = 0  # số lượng câu
    w = 1  # số lượng từ (bắt đầu là 1 vì không có khoảng trắng đầu tiên)

    for char in text:
        if char.isalpha():
            l += 1
        if char == ' ':
            w += 1
        if char in ['.', '?', '!']:
            s += 1

    index = 0.0588 * (l / w) * 100 - 0.296 * (s / w) * 100 - 15.8
    return round(index)

def main():
    text = input("Text: ")
    grade = coleman(text)
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")

if __name__ == "__main__":
    main()
