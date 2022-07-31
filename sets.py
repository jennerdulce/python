# BUT, if what we need is to remove duplicates, or do mathematical operations like combining lists (unions), we can, and SHOULD always use sets.
# Sets do not contain duplicates
some_set = {1, 2, 3, 4, 5}

# Test for duplicates
def set_duplicates():
    # Potentially retuns unordered list
    my_list = [1, 2, 3, 2, 3, 4]
    no_dups = list(set(my_list))
    print(no_dups)

# set_duplicates()

# Test for membership
# Sets have an O(1) time when checking for contents within a set

def membership_example(num):
    if num in some_set:
        print(True)
    else:
        print(False)

# membership_example(1)
# membership_example(99)

def add_to_set(num):
    some_set.add(num)
    print(some_set) 

# add_to_set(99) # {1, 2, 3, 4, 5, 99}
# add_to_set(1) # Does not add duplicates: {1, 2, 3, 4, 5, 99}

def update_set(arr):
    some_set.update(arr)
    print(some_set)

some_arr = [4, 5, 'a', 'b', 'c'] # Does not add 4 and 5 to set because they are duplicates
# update_set(some_arr) # some_set = {1, 2, 3, 4, 5}

# Remove / Discard, also pop() and clear()
def remove_discard(action, value):
    print(f'Original: {some_set}')
    if action == 'remove':
        print(f'Removing: {value}')
        some_set.remove(value)
    else:
        print(f'Discarding: {value}')
        some_set.discard(value)
    print(some_set)

# remove_discard('remove', 1)
# remove_discard('discard', 5)

def combind_sets(set_1, set_2):
    print(f'Set 1: {set_1}')
    print(f'Set 2: {set_2}')
    union_set = set_1.union(set_2)
    # union_set = set_1 | set_2
    print(f'Union: {union_set}')

set_a = {1, 2, 3}
set_b = {1, 4, 5, 6, 2, 3}
# combind_sets(set_a, set_b)

def set_intersection(set_1, set_2):
    print(f'Set 1: {set_1}')
    print(f'Set 2: {set_2}')
    # intersection_set = set_1.intersection(set_2)
    intersection_set = set_1 & set_2
    print('Intersection at: ')
    print(intersection_set)

set_intersection(set_a, set_b)

def set_difference(set_1, set_2):
    # Only returns the difference that are unique to the first set
    print(set_1.difference(set_2))

# set_difference(set_a, set_b)

def set_symetric_difference(set_1, set_2):
    print(set_1.symetric_difference(set_2))

set_symetric_difference(set_a, set_b)
