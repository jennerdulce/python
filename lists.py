numbers = [69, 1337, 1, 8008, 100, 9000]
colors = ['red', 'blue', 'green', 'orange', 'yellow']

def indexes():
    print(f'this is [0]: {numbers[0]}')
    print(f'this is [-1]: {numbers[-1]}')

# indexes()

def slice_example():
    print(numbers[0:3]) # NOT INCLUSIVE; prints indexes: 0, 1, 2
    print(numbers[1:]) # [1337, 8008, 100, 9000]
    print(numbers[:2]) # [69, 1337]

# slice_example()

# Slicing will create a new copy ****
def copy_example():
    new_numbers = numbers[:]
    new_numbers.append(1)
    print(f'numbers: {numbers} length: {len(numbers)}')
    print(f'new_numbers: {new_numbers} length: {len(new_numbers)}')

# copy_example()

def replace_index(index, new_string):
    print(numbers)
    numbers[index] = new_string
    print(numbers)

# replace_index(1, 'testing')

def concatenation_and_replication():
    nums = [1, 2, 3]
    chars = ['a', 'b', 'c']
    print(f'nums + chars: {nums + chars}') # combinds
    print(f'chars * 2: {chars * 2}')

# concatenation_and_replication()

def looping_lists():
    # similar to for each
    for num in numbers:
        print(num)

# looping_lists()

def enumerate_example():
    # Similar to forEach loops and using index / value parameters
    for index, num in enumerate(numbers):
        print(f'index: {index} - value: {num}')

# enumerate_example()

prices = ['.90', '1', '.50', '2']
fruits = ['banana', 'apple', 'grape', 'sweet potato']
def zip_example():
    # iterating through 2 array at the same time
    for price, fruit in zip(prices, fruits):
        print(f'{fruit} costs: ${price}')

# zip_example()

def in_and_not_in():
    # Similar to .includes()
    print('banana' in fruits)
    print('watermelon' in fruits)
    print('salad' not in fruits)

# in_and_not_in()

def multiple_assign():
    # Sort of like destructuring
    colors = ['blue', 'red', 'green']
    blue, red, green = colors
    print(blue)
    # print(red)
    # print(green)

# multiple_assign()

def swap_trick():
    a, b = 1, 99
    print(f'This is a: {a}')
    print(f'This is b: {b}')
    print("======= SWAP =======")
    a, b = b, a
    print(f'This is a: {a}')
    print(f'This is b: {b}')

# swap_trick()

def finding_index():
    # Finds only the first index
    furniture = ['table', 'chair', 'rack', 'shelf', 'chair']
    print(furniture.index('chair'))
    
# finding_index()

def append_and_insert():
    copy_colors = colors[:]
    print(copy_colors)
    copy_colors.append('BLACK')
    copy_colors.insert(1, 'WHITE')
    print(copy_colors)

# append_and_insert()

def del_remove_pop():
    copy_colors = colors[:]
    print(copy_colors)
    del copy_colors[0] # removes at index
    print(copy_colors)
    copy_colors.remove('green') # removes by value
    print(copy_colors)
    # removes at end or at index. ** RETURNS REMOVED VALUE **
    copy_colors.pop() 
    print(copy_colors)

# del_remove_pop()

def sort_reverse():
    copy_numbers = numbers[:]
    print(f'BEFORE: {copy_numbers}')
    copy_numbers.sort()
    print(f'AFTER: {copy_numbers}')
    copy_numbers.sort(reverse=True)
    print(f'REVERSED: {copy_numbers}')

# sort_reverse()

def sort_alphabetical():
    letters = ['a', 'z', 'A', 'Z', 'c', 't', 'T', 'C']
    print(f'BEFORE: {letters}')
    letters.sort(key=str.lower)
    print(f'AFTER: {letters}')

# sort_alphabetical()

def sorted_method():
    sorted_numbers = sorted(numbers)
    print(f'ORIGINAL: {numbers}')
    print(f'SORTED: {sorted_numbers}') # returns newly sorted array without affecting original
    print(f'ORIGINAL DOES NOT CHANGE: {numbers}')

# sorted_method()

def tuple_example():
    copy_nums = numbers[:]
    arr = tuple(copy_nums)
    print(arr)
    print(arr[0])
    # arr.pop(0) Does not work

# tuple_example()

def list_example():
    # Similar to .split()
    some_str = 'hello there'
    split_str = list(some_str)
    print(split_str)

# list_example()