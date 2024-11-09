def main():
    list = [ "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
    while True:
        try:
            outdated = input("Date: ").strip()
            month, day, year = check(outdated)
            day = int(day)
            year = int(year)
            if month.isalpha() and month in list:
                if 0 < day < 32:
                    month = list.index(month)
                    month += 1
                    print(f"{year}-{month:02}-{day:02}")
                    break
            elif month.isdigit():
                month = int(month)
                if month < 13 and 0 < day < 32:
                    print(f"{year}-{month:02}-{day:02}")
                    break
        except (ValueError, TypeError):
            pass
def check(outdated):
    try:
        if '/' in outdated:
            month, day, year = outdated.split('/')
            if month.isalpha():
                return ValueError
        elif ' ' in outdated and ',' in outdated:
            month, day, year = outdated.split()
            day = day.replace(",", "")
        return month, day, year
    except UnboundLocalError:
        pass
main()
