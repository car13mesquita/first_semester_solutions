# Author: CAM (AMDG) 11/3/2021

user_string = input("Enter a string: ")
string_length = len(user_string)
split_value = int(string_length / 2)

first_half = user_string[:split_value]
second_half = user_string[split_value:]

print("The first half of the string is: '" + first_half + "'.")
print("The second half of the string is: '" + second_half + "'.")

