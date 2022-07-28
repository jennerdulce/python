# While Loops
def basic_while():
    counter = 0
    while counter < 5:
        print('I love Karen')
        counter += 1

# basic_while()

def enter_name():
    while True:
        name = input('Please enter your name: ')
        if not name:
            print('Hey you really need to enter your name')
            continue
        else:
            print('Hey {}, Thank you for entering your name!'.format(name))
            break
    print('Access Granted')

# enter_name()

def for_looping():
    colors = ['red', 'blue', 'green']
    for color in colors:
        print(color)

# for_looping()

def range_function():
    for i in range(5):
        print(i)
# 0
# 1
# 2
# 3
# 4
# range_function()

def range_function_with_parameters():
                # start # stop # step
    for i in range(1, 6, 1):
        print(i)
# 1
# 2
# 3
# 4
# 5
# range_function_with_parameters()

def for_else_loop():
    for i in [1, 2, 3, 4, 5]:
        if i == 3:
            print('Stopping executing')
            break
        else:
            print('Executing')

# for_else_loop()
import sys

def sys_exit():
    while True:
        feedback = input('Type exit to exit: ')
        if feedback == 'exit':
            print(f'You typed "{feedback}"')
            sys.exit()
        print('Please type exit')
        
sys_exit()