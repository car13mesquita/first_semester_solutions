# Author: CAM (AMDG) 12/2/2020


def sum_to_odd(lst):
    total = 0
    iteration = 0
    while iteration < len(lst):
        if lst[iteration] % 2 == 0:
            total += lst[iteration]
            iteration += 1
        else:
            return(total)
    return(total)


print(sum_to_odd([2, 4, 6, 8, 9]) == 20)
print(sum_to_odd([13, 12, 10]) == 0)
print(sum_to_odd([14, 16, 32]) == 62)
