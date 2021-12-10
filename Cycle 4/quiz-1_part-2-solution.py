# Author: CAM (AMDG)  10/19/2021

year = input("Enter the year of the date: ")
month = input("Enter the month of the date: ")
day = input("Enter the day of the date: ")

q = int(day)
m = int(month)
y = int(year)

if month == "1":
    m = 13
    y -= 1

if month == "2":
    m = 14
    y -= 1

j = y // 100
k = y % 100

h = (q + ((26 * (m + 1)) // 10) + k + (k//4) + (j//4) + (5 * j)) % 7

if h == 0:
    day_of_week = "Saturday."
elif h == 1:
    day_of_week = "Sunday."
elif h == 2:
    day_of_week = "Monday."
elif h == 3:
    day_of_week = "Tuesday."
elif h == 4:
    day_of_week = "Wednesday."
elif h == 5:
    day_of_week = "Thursday."
elif h == 6:
    day_of_week = "Friday."

print('\n' + month + "/" + day + "/" + year + " was a " + day_of_week)
