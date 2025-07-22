#!/usr/bin/env python3

number_str = input("Give me a number: ")
try:
    number = float(number_str)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a number.")
