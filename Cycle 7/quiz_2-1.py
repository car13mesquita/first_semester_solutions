# Author CAM (AMDG) 02/23/2020

day = input("What letter day is it (A-G)?: ")

class_meets = ['A', 'C', 'E']
no_class = ['B', 'D', 'F', 'G']

if day.upper() in class_meets:
    print("You have class today because it is {0} day.".format(day.upper()))
elif day.upper() in no_class:
    print("You do not have class today because it is {0} day.".format(day.upper()))
else:
    print("You did not enter a valid input. Please try again.")
