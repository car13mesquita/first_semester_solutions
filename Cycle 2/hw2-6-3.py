# Author: CAM (AMDG) 9/26/2020

free_throws = input("How many free throws did the player score? ")
two_pointers = input("How many two pointers did the player score? ")
three_pointers = input("How many three pointers did the player score? ")

total_points = int(free_throws) + int(two_pointers) * 2 + int(three_pointers) * 3

print("The player scored " + str(total_points) + " points in the game.")
