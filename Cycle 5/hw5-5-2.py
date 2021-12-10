# Author: CAM (AMDG) 11/3/2021

user_string = input("Enter a six letter word: ")

odd_string = user_string[0] + user_string[2] + user_string[4]
joined_odd_string = '-'.join(odd_string)

even_string = str(user_string[1] + user_string[3] + user_string[5])
joined_even_string = '-'.join(even_string)

print("The odd characters in the word are : " + joined_odd_string)
print("The even characters in the word are: " + joined_even_string)
