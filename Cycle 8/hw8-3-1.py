# Author: CAM (AMDG) 12/2/2020


def count_odds(lst):
    num_odds = 0
    iteration = 0
    while iteration < len(lst):
        if lst[iteration] % 2 != 0:
            num_odds += 1
        iteration += 1
    return(num_odds)


print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)
