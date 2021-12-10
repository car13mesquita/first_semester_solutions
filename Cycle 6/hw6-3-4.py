# Author: CAM (AMDG) 11/15/2020

items = input("Enter a list of items separated by spaces: ")
lst = items.split()

ends_middle = input("Do you want the middle or the ends? ")

if ends_middle.lower() == 'middle':
    middle = lst[1:-1]
    print("The middle of {0} is {1}".format(items, middle))
elif ends_middle.lower() == 'ends':
    ends = []
    ends.append(lst[0])
    ends.append(lst[-1])
    print("The ends of {0} are {1}".format(items, ends))
else:
    print("Input not recognized. Please try again.")
