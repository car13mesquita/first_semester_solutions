# Author: CAM (AMDG) 12/2/2020


def count_letter(word, letter):
    occurrences = 0
    iteration = 0
    while iteration < len(word):
        if word[iteration] == letter:
            occurrences += 1
        iteration += 1
    return(occurrences)


print(count_letter("cat", "t") == 1)
print(count_letter("apple", "p") == 2)
print(count_letter("supercalifragilisticexpialidocious", "i") == 7)
