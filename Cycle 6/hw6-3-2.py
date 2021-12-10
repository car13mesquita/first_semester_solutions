# Author: CAM (AMDG) 11/15/2020

values = input("Enter a sequence of values separated by spaces: ")
lst = values.split()

lst_copy = lst.copy()
lst_copy.sort()

if lst == lst_copy:
    print("The list of values ({0}), is sorted.".format(values))
elif lst != lst_copy:
    print("The list of values ({0}), is not sorted.".format(values))
else:
    print("Error")