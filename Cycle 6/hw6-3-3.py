# Author: CAM (AMDG) 11/15/2020

numbers = input("Enter a sequence of 5 numbers separated by spaces: ")
lst = numbers.split()

total = int(lst[0]) + int(lst[1]) + int(lst[2]) + int(lst[3]) + int(lst[4])

print("The values {0} total to {1}".format(numbers, total))

