def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
# Nếu chia 2 dòng thì khi check đk 1 thoả thì sẽ return luôn và ko check đk 2 nên cần viết 1 dòng
    if 2 <= len(s) <= 6 and start(s) and number(s) and allow(s):
        return True
    else:
        return False

def start(n):
    n = str(n)
    if n[0:2].isalpha():
        return True
    else:
        return False

def number(i):
    i = str(i)
# check từ chứ thứ 3
    if i[2] == '0':
        return False
# phải cho ngoài vòng loop nếu trong thì i[2] sẽ check từ chữ thứ 5 thay vì thứ 3
    i = i[2:]
    for c in range(len(i)):
        if i[c].isdigit():
# i[c] truy cập phần tử ở c trong dãy i.
# if i is the string 'hello' and c is 1, then i[c] would be 'e'
            for m in range(c, len(i)):
                if not i[m].isdigit():
                    return False
            return True
    return True

def allow(m):
    for c in m:
        if c in [".", ",", " ", "'", "?", "()", "{", "}", "!", "-", "_"]:
            return False
    return True

main()
