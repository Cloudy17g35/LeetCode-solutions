'''Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.'''

from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = date(year, month, day)
        
        return d.strftime('%A')
