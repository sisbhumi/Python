#----------------------- Map function ------------------#
# Return double of n
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# output: [2, 4, 6, 8]

#---------------------------------------------------#

# Double all numbers using map and lambda

number = (1, 2, 3, 4)
result = map(lambda x: x*3, number)
print(list(result))

#output: [3, 6, 9, 12]

#------------------------ Reduce Function ----------------------------#

import functools

lis = [1, 3, 5, 6, 2, ]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

"""
Output:
The sum of the list elements is : 17
The maximum element of the list is : 6
"""

#----------------------------------------------------#

num_list = [1,2,3,4,5]
max_num = functools.reduce(lambda x,y: x if x > y else y, num_list)
print(max_num)
#Output: 5

#----------------------------- Filter ----------------------#

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False
def filter_consonants(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return False if letter in vowels else True

filtered_vowels = filter(filter_vowels, letters)
filtered_consonants = filter(filter_consonants, letters)
vowels = tuple(filtered_vowels)
consonants = tuple(filtered_consonants)
print(vowels)
print(consonants)

"""
Output:
('a', 'e', 'i', 'o')
('b', 'd', 'j')
"""

#--------------------------------------------------#
numbers = [1, 2, 3, 4, 5, 6, 7]

even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

even_numbers = list(even_numbers_iterator)

print(even_numbers)

#Output: [2, 4, 6]

