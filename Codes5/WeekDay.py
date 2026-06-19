class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def is_leap(y:int) -> bool :
            return y%4==0 and (y%100!=0 or y%400==0)
        days_of_week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total= 0
        for y in range(1971,year):
            total+= 366 if is_leap(y) else 365
        for m in range(1,month):
            if m==2 and is_leap(year):
                total+=29 
            else:
                total+=days_in_months[m]
        total+=day-1
        return days_of_week[total%7]
