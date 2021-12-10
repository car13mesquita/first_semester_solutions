# Author: CAM (AMDG) 12/2/2020


def sum_odds(lst):
    total = 0
    for num in lst:
        if num % 2 != 0:
            total += num
    return(total)


print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)
