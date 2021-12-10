# Author: CAM (AMDG) 12/2/2020


def three_letter_words(lst):
    num_three_letter = 0
    iteration = 0
    while iteration < len(lst):
        if len(lst[iteration]) == 3:
            num_three_letter += 1
        iteration += 1
    return(num_three_letter)


print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
