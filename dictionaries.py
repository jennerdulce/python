fang = {
    'name': 'Fang',
    'age': 5,
    'color': 'Grey',
    'plays_fetch': False,
    'tail': 'curly',
    'sheds': 'A lot'
}

def values_method():
    # Finds all values
    all_values = []
    for value in fang.values():
        all_values.append(value)
    print(all_values)

# values_method()

def keys_method():
    # Finds all values
    all_keys = []
    # This list is immutable and you cannot work with it
    print(fang.keys())
    for key in fang.keys():
        all_keys.append(key)
    print(all_keys)

# keys_method()

def keys_and_values():
    # Use the items() method on objects
    for key, value in fang.items():
        print(f'Key: {key} - Value: {value}')

# keys_and_values()

def check_key_value():
    print('name' in fang.keys())
    print('hair' in fang.keys())
    print(5 in fang.values())
    print('white' in fang.values())

# check_key_value()

def get_values():
    print(f'My dog\'s name is {fang.get("name")}')
    print(fang["name"])

# get_values()

def adding_values(key, value):
    if key not in fang:
        fang[key] = value
    print(fang)

# adding_values('dumb', True)
# adding_values('stinky', True)

# Pretty Printing
import pprint

def pprint_example():
    print(fang)
    # {'name': 'Fang', 'age': 5, 'color': 'Grey', 'plays_fetch': False, 'tail': 'curly', 'sheds': 'A lot'}
    pprint.pprint(fang)

    #   {'age': 5,
    #  'color': 'Grey',
    #  'name': 'Fang',
    #  'plays_fetch': False,
    #  'sheds': 'A lot',
    #  'tail': 'curly'}

# pprint_example()

color_pallette_a = {'col_1': 'blue', 'col_2': 'pink', 'col_3': 'light-blue'}
color_pallette_b = {'col_1': 'red', 'col_2': 'pink', 'col_3': 'orange'}
def merge_dictionaries(dict1, dict2):
    # Second dictionary overtakes the other and replaces values
    combind_dict = {**dict1, **dict2}
    # {'col_1': 'red', 'col_2': 'pink', 'col_3': 'orange'}
    pprint.pprint(combind_dict)

merge_dictionaries(color_pallette_a, color_pallette_b)

