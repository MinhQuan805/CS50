def main():
    expression = input("Expression: ")
    x, y, z = expression.split()
    x = float(x)
    z = float(z)
    result = calculate(x, y, z)
    print(f"{result:.1f}")
def calculate(x, y, z):
    import operator
    if y == '+':
        return operator.add(x, z)
    elif y == "-":
        return operator.sub(x, z)
    elif y == "*":
        return operator.mul(x, z)
    elif y == "/":
        return operator.truediv(x, z)
# Không cần dùng operator nhưng do có ý tưởng hỏi gpt nên vậy, dùng print result = x + y là được
main()


