# library  fine calculator
from datetime import date

day = int(input(" enter the issue date "))
mon = int(input(" enter the issue month "))

re_day = int(input(" enter the return date "))
re_mon = int(input(" enter the return month "))


issue_date = date(2025, mon, day)
return_date = date(2025, re_mon, re_day)

date_diff = (return_date - issue_date).days


overday = 15

late = date_diff - overday

if late > 10:
    print(" days cancelled1")

else:
    print(" congratulations ")
