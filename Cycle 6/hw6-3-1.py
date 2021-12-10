# Author: CAM (AMDG) 11/15/2020

word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

word1_lst = list(word1)
word2_lst = list(word2)

word1_lst.sort()
word2_lst.sort()

if word1_lst == word2_lst:
    print("{0} and {1} are anagrams.".format(word1, word2))
elif word1_lst != word2_lst:
    print("{0} and {1} are not anagrams.".format(word1, word2))
else:
    print("Error")
