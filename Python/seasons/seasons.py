from datetime import date
import sys
import inflect
p = inflect.engine()
class Seasons:
    def __init__(self, year, month, day):
        if not year.isdigit() or not month.isdigit() or not day.isdigit():
            sys.exit("Invalid date")
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
    @classmethod
    def get_date(cls):
        date = input("Date of Birth: ")
        if "-" not in date:
            sys.exit("Invalid date")
        year, month, day = date.split("-")
        return year, month, day
    @classmethod
    def calculate(cls, year, month, day):
        today = date.today()
        now_year, now_month, now_day = map(int, str(today).split("-"))
        # set date start and date end
        start = date(int(year), int(month), int(day))
        end = date(now_year, now_month, now_day)
        # calculate days
        count_day = end - start
        # calcualte minutes
        minutes_count = count_day.total_seconds() / 60
        return minutes_count
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        if year < 0:
            sys.exit("Invalid date")
        self._year = year

    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, month):
        if month > 12 or month < 1:
            sys.exit("Invalid date")
        self._month = month

    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, day):
        if day < 1 or day > 31:
            sys.exit("Invalid date")
        self._day = day

def main():
    try:
        # Call values from Seasons class to use for calculate
        year, month, day = Seasons.get_date()
        result = Seasons.calculate(year, month, day)
        words = p.number_to_words(int(result), andword="")
        words = words.capitalize()
        print(f"{words} minutes")
    except ValueError:
        sys.exit("Invalid date")
if __name__ == "__main__":
    main()
