#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
greater = "and is greater than 5"
zero = "and is 0"
less_than = "and is less than 6 and not 0"
if number >= 0:
    last_digit = number % 10
if number < 0:
    last_digit = number % -10
if last_digit > 5:
    print(f"{str1} {number:d} is {last_digit:d} {greater}")
elif last_digit == 0:
    print(f"{str1} {number:d} is {last_digit:d} {zero}")
else:
    print(f"{str1} {number:d} is {last_digit:d} {less_than}")
