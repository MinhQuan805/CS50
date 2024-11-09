my_dict = {}
while True:
    try:
        while True:
            item = input().lower()
            if item in my_dict:
                my_dict[item] += 1
            else:
                my_dict[item] = 1
    except EOFError:
        for i in my_dict:
            print(my_dict[i],  i.upper(), sep=" ", end='\n')
        break

