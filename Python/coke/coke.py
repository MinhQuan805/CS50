amount_due = 50
m = [5,10,25]
print("Amount Due:", amount_due)
while amount_due > 0:
    m = [5,10,25]
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in m:
        newtotal = amount_due - coin

        if newtotal > 0:
            print("Amount Due: ", newtotal)
            amount_due = newtotal

        if newtotal <= 0:
            newtotal = abs(newtotal)
# abs() là funtions return giá trị tuyệt đối, nên phải gán cho variable
            print(f"Change Owed: {newtotal}")
            break

    else:
        print("Amount Due: ", amount_due)
