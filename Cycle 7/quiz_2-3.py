# Author CAM (AMDG) 02/23/2020

import random

user_numbers = input("Enter 3 numbers separated by spaces: ")

nums = user_numbers.split()

winning_nums = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'], k=3)

correct_numbers = 0

if winning_nums[0] in nums:
    correct_numbers += 1
if winning_nums[1] in nums:
    correct_numbers += 1
if winning_nums[2] in nums:
    correct_numbers += 1

if correct_numbers == 3:
    print("The winning numbers are {0}, {1}, and {2}. You won!".format(winning_nums[0], winning_nums[1], winning_nums[2]))
elif correct_numbers == 2:
    print("The winning numbers are {0}, {1}, and {2}. You got two numbers correct!".format(winning_nums[0], winning_nums[1], winning_nums[2]))
elif correct_numbers == 1:
    print("The winning numbers are {0}, {1}, and {2}. You got one number correct!".format(winning_nums[0], winning_nums[1], winning_nums[2]))
else:
    print("The winning numbers are {0}, {1}, and {2}. You got none correct.".format(winning_nums[0], winning_nums[1], winning_nums[2]))