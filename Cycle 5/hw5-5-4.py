# Author: CAM (AMDG) 11/3/2021

user_string1 = input("Enter a word: ")
user_string2 = input("Enter another word: ")
user_string3 = input("Enter one final word: ")

if user_string1.islower() == False:
    corrected_string1 = user_string1.lower()
else:
    corrected_string1 = user_string1

if user_string2.islower() == False:
    corrected_string2 = user_string2.lower()
else:
    corrected_string2 = user_string2

if user_string3.islower() == False:
    corrected_string3 = user_string3.lower()
else:
    corrected_string3 = user_string3

if corrected_string1 < corrected_string2 and corrected_string2 < corrected_string3:
    print("{0}, {1}, {2}".format(user_string1, user_string2, user_string3))
elif corrected_string1 < corrected_string3 and corrected_string3 < corrected_string2:
    print("{0}, {1}, {2}".format(user_string1, user_string3, user_string2))
elif corrected_string2 < corrected_string1 and corrected_string1 < corrected_string3:
    print("{0}, {1}, {2}".format(user_string2, user_string1, user_string3))
elif corrected_string2 < corrected_string3 and corrected_string3 < corrected_string1:
    print("{0}, {1}, {2}".format(user_string2, user_string3, user_string1))
elif corrected_string3 < corrected_string1 and corrected_string1 < corrected_string2:
    print("{0}, {1}, {2}".format(user_string3, user_string1, user_string2))
elif corrected_string3 < corrected_string2 and corrected_string2 < corrected_string1:
    print("{0}, {1}, {2}".format(user_string3, user_string2, user_string1))
else:
    print("Error")
