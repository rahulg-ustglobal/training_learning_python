import datetime
from datetime import date

year1=int(input("Enter year1:="))
month1=int(input("Enter month1:="))
day1=int(input("Enter day1:="))
x=date(year1,month1,day1)

year2=int(input("Enter year2:="))
month2=int(input("Enter month2:="))
day2=int(input("Enter day2:="))

y=date(year2,month2,day2)

date_diff=y-x
print(date_diff)
dt=datetime.datetime.today()
#1)Find the year
print(dt.year)
#2)Find the month
print(dt.month)
#3)Find the day
print(dt.day)