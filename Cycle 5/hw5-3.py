# Author: CAM (AMDG) 11/3/2021

import calendar

# Question 1
calendar.TextCalendar().pryear(2021)

# Question 2
calendar.TextCalendar(6).pryear(2021)

# Question 3
calendar.prmonth(2021, 11)

# # # Question 4
# # calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)
# # calendar.LocaleTextCalendar(6, "FRENCH").pryear(2020)
# # # calendar.LocaleTextCalendar(6, "KLINGON").pryear(2020)

# Question 5
print(calendar.isleap(2020))
print(calendar.isleap(2019))
