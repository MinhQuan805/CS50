def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    totalorder = 0
    i = 0
    while i < 1:
        try:
            order = check(menu)
            neworder = totalorder + menu[order]
            print(f"Total: ${neworder:.2f}")
            totalorder = neworder
        except EOFError:
            print("")
            break

def check(menu):
    while True:
        order = input("Item: ")
        order = order.title()
        if order in menu:
            return order

main()

