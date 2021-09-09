class Solution:
    def dayOfYear(self, date: str) -> int:
        months = {1: 31, 2: 28, 3: 31, 4: 30,
                  5: 31, 6: 30, 7: 31, 8: 31,
                  9: 30, 10: 31, 11: 30, 12: 31}
        year, month, day = date.split("-")
        year, month, day = int(year), int(month),int(day)

        total_days = 0

        if month == 1:
            return day
        else:
            if year % 4:
                for i in range(1,month):
                    total_days += months[i]
            else:
                for i in range(1, month):
                    if i == 2:
                        months[i] = 29
                    total_days += months[i]
        return total_days + day
