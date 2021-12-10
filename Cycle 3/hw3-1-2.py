# Author: CAM (AMDG) 10/3/2020

first_card = int(input("What is the value of your first card? "))
second_card = int(input("What is the value of your second card? "))

card_total = first_card + second_card

if card_total > 21:
    print("You lose.")
else:
    print("You win!")
