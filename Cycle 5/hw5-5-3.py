# Author: CAM (AMDG) 11/3/2021

user_string = input("Enter a word: ")

reversed_user_string = user_string[::-1]

if user_string == reversed_user_string:
    print("{0} reversed is {1}. Which means it is a palindrome!".format(user_string, reversed_user_string))
else:
    print("{0} reversed is {1}. Which means it is not a palindrome.".format(user_string, reversed_user_string))
