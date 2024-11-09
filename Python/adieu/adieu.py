import inflect

p = inflect.engine()
l = []
while True:
    try:
        name = input("Name: ")
        l.append(name)
    except EOFError:
        print()
        break
output = p.join(l)

hi = "Adieu, adieu, to " + output
print(hi)


