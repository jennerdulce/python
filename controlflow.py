# Comparison Operators
# ==
# !=
# <
# >
# <=
# >=

print(42 == 42) # true
print(1 != 0) # true
print(0 < 2) # true
print(2 < 0) # false
print(3 > 3) # false
print(4 > 2) # true
print(1 <= 10) # true
print(1 <= 0) # false
print(99 >= 99) # true
print(99 >= 100) # false

# Boolean Operators
print((4 < 5) and (5 < 6)) # true 
print((4 < 5) and (9 < 6)) # false
print(not (1 == 2) or (1 == 2)) # true

# If Statements
name = 'Karen'
if name == 'Jenner':
    print('Hi, {}'.format(name))
elif name == 'Karen':
    print('Hi, {}'.format(name))
else:
    print('Hey What\'s Up!')

# Ternary Conditional Operator
age = 21
if age >= 21:
    print('You can drink')
else:
    print('You cannot drink. Get out of here')

print('Adult' if age >= 21 else 'Kid')