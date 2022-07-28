# Return Values
def sum_two_numbers(num_1, num_2):
    return num_1 + num_2
result = sum_two_numbers(4, 6)
print(result)

some_global_variable = 'I AM INEVITABLE'
def some_function():
    print(some_global_variable)
    local_variable = 'only availabile inside this function'
    print(local_variable)

some_function()
# print(local_variable) make an error

def spam():
    global eggs # targets eggs outside the function
    eggs = 'CHANGE EGGS VALUE'

eggs = 'This is eggs'
spam()
print(eggs)

def add(x, y):
    return x + you

lambda_add = lambda x, y: x + y
added_numbers = lambda_add(100, 99)
print(added_numbers)

def make_adder(n):
    return lambda x: x + n

plus_300 = make_adder(300)
print(plus_300(99))