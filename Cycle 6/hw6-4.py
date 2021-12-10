lst = ['one', 'two', 'three']
lst.reverse()
print(lst)

lst = [1, 4, 5, 6, 3, 7, 8, 0, 2, 9]
lst.sort()
print(lst)

lst = ['this', 'sentence', 'is', 'false']
print(lst.index('is'))

lst = ['a', 'b', 'c', 'd']
lst.append(['e', 'f', 'g'])
print(lst)

lst = ['a', 'b', 'c', 'd']
lst.extend(['e', 'f', 'g'])
print(lst)

lst = ['red', 'blue', 'green']
lst.clear()
print(lst)

lst = ['a', 'a', 'a', 'a']
lst.remove('a')
print(lst)

lst = ['a', 'b', 'c', 'd']
lst.insert(2, 'letters')
print(lst)

lst = ['a', 'b', 'c', 'd']
lst[2] = "f"
print(lst)

lst = ['a', 'b', 'c', 'd']
del lst[2]
print(lst)
