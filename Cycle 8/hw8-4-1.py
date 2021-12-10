# Author: CAM (AMDG) 12/11/2020

from random import randint

comp_num = randint(0, 50)

while True:
    user_num = input("I'm thinking of a number between 0 and 50. What do you think the number is? ")

    if user_num == "stop":
        print("The number I was thinking of was {0}.".format(comp_num))
        break
    elif user_num.isdigit():
        integer_num = int(user_num)
    else:
        print("Please enter a number")
        continue

    if integer_num > comp_num:
        print("Lower")
    elif integer_num < comp_num:
        print("Higher")
    else:
        print("You guessed {0}, which is correct!".format(integer_num))
        break
