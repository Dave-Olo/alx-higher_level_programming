#!/usr/bin/python3
for figure in range(0, 100):
    if figure in [99]:
        print("{:d}".format(figure))
        break
    print("{:02d}, ".format(figure), end='')
