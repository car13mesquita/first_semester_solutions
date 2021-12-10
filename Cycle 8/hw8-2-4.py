# Author: CAM (AMDG) 12/2/2020


def count_letter(word, letter):
    occurrences = 0
    for character in word:
        if character == letter:
            occurrences += 1
    return(occurrences)


print(count_letter("cat", "t") == 1)
print(count_letter("apple", "p") == 2)
print(count_letter("supercalifragilisticexpialidocious", "i") == 7)
