# Author: CAM (AMDG) 12/2/2020


def three_letter_words(lst):
    num_five_letter = 0
    for word in lst:
        if len(word) == 3:
            num_five_letter += 1
    return(num_five_letter)


print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)
