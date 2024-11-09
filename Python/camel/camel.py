s = input("camelCase: ")
snake_case =""
# snake_case ="" nói cho python biết rằng snake_case là một string và được define
for c in s:
    if c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case += c
print("snake_case:",snake_case)

