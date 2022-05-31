#!/usr/bin/python3
for figure1 in range(0, 10):
    for figure2 in range(1, 10):
        if figure1 == 8 and figure2 == 9:
            print("{:d}{:d}".format(figure1, figure2))
            break
        if figure2 > figure1:
            print("{:d}{:d}, ".format(figure1, figure2), end='')
