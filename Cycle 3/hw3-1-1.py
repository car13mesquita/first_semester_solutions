# Author: CAM (AMDG) 10/3/2020

a_wins = int(input("How many wins did the first team have? "))
a_ties = int(input("How many ties did the first team have? "))

b_wins = int(input("How many wins did the second team have? "))
b_ties = int(input("How many ties did the second team have? "))

a_wins *= 3
b_wins *= 3

a_total = a_wins + a_ties
b_total = b_wins + b_ties

if a_total == b_total:
    print("It's a tie.")
else:
    if a_total > b_total:
        print("Team A wins!")
    else:
        print("Team B wins!")
