def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):
    percentage = float((p).replace("%", ""))
# tôi gặp lỗi khúc này vì chưa replace thay p thành string mà lúc này tôi chưa chuyển nó thành number nên ko tính đc
    decimal = percentage / 100
    return decimal


main()