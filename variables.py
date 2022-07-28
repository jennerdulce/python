# Expressions
print(2 + 3)
print(2 - 3)
print(2 * 6)
print(3 % 2)

# Data Types
# String
hello = 'hello'
world = 'world'

# Number
number = 1
number += 9
print(number)

# Variable naming convention
snake_case = 'This is the proper naming convention'

# Flag
flag_string = 'Hello I am a flag!'
print('This is a flag:', flag_string) 
# This is a flag: Hello I am a flag!

# `end`: refrains from creating a new line
some_sentence = ['this', 'is', 'a', 'sentence']
for word in some_sentence:
    print(word)
# this
# is
# a
# sentence

# for word in some_sentence:
#     print(word, end='-')
#this-is-a-sentence                                                       
# `sep`: specify how to separate objects
print('red', 'blue', 'green', sep=',')

# `input()`: takes user input and converts into a string
# my_name = input('What is your name? ')
# print('Hi, {}'.format(my_name))

# `len()`: evaluates to integer value
colors = ['red', 'blue', 'green']
length_of_colors = len(colors)
print(length_of_colors)

# Testing for emptiness: testing for arr is truthy
arr = []
if arr:
    print('not empty')
else:
    print('empty')

# Data type conversions
# str()
# int()
# float()