#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_str = sys.argv[1]
    z_list = [char for char in input_str if char == "z"]

    if z_list:
        print("z" * len(z_list))
    else:
        print("none")
