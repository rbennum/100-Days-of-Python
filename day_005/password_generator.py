import string
import random

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(0, letters_count):
    password_list.append(random.choice(string.ascii_letters))

for char in range(0, symbols_count):
    password_list.append(random.choice(string.punctuation))

for char in range(0, numbers_count):
    password_list.append(random.choice(string.digits))

random.shuffle(password_list)

print(''.join(password_list))
