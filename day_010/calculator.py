import os
import sys

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def math_op(first_op, operator, second_op):
    if first_op is None or second_op is None:
        return None
    if operator == '+':
        return first_op + second_op
    elif operator == '-':
        return first_op - second_op
    elif operator == '*':
        return first_op * second_op
    elif operator == '/':
        return first_op / second_op
    else:
        return None

def input_num(prompt):
    try:
        return float(input(prompt))
    except:
        return None

def input_op(prompt):
    op = input(prompt)
    if op in ['+','-','/','*']:
        return op
    else:
        return None

def calculator():
    calc_asset = r'''

    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|

    '''
    should_continue = False
    first_op = 0.0
    operator = None
    second_op = 0.0
    while True:
        if should_continue:
            operator = input_op("Pick an operation (+,-,*,/): ")
            second_op = input_num("What's the next number: ")
        else:
            print(calc_asset)
            first_op = input_num("What's the first number: ")
            operator = input_op("Pick an operation (+,-,*,/): ")
            second_op = input_num("What's the next number: ")
        result = math_op(first_op, operator, second_op)
        print(f"{first_op} {operator} {second_op} = {result}")
        next_stage = input(
f"""
Type:
    - 'y' to continue calculating with {result},
    - 'n' to start a new calculation,
    - 'q' to quit.
"""
        )
        should_continue = next_stage == 'y'
        should_quit = next_stage == 'q'
        if should_quit:
            print("Good bye!")
            sys.exit()
        if should_continue:
            first_op = result
        else:
            clear()

try:
    calculator()
except KeyboardInterrupt:
    print('Good bye!')