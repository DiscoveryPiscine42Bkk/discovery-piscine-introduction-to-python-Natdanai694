#!/usr/bin/env python3

import math

number_str = input("Give me a number: ")
try:
    number = float(number_str)
    rounded = math.ceil(number)
    print(rounded)
except ValueError:
    print("Invalid input. Please enter a number.")
