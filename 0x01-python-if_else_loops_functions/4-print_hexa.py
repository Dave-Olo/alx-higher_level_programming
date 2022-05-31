#!/usr/bin/python3
# Printing numbers from 0 to 98 in decimal(base 10) and hexadecimal(base 16)
for num in range(0, 99):
    print("{:d} = 0x{:x}".format(num, num))
