#!/usr/bin/python3
'''sandglass module'''


def sandglass(size):
    '''prints sandglass using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        spaces_number = 0
        astrics_number = (size * 2) - 1
        i = size

        while i > 0:
            for space in range(spaces_number):
                print(' ', end='')
            for astric in range(astrics_number):
                print('*', end='')
            print()
            spaces_number += 1
            astrics_number -= 2
            i -= 1

        spaces_number = size - 2
        astrics_number = 3

        while i < size - 1:
            for space in range(spaces_number):
                print(' ', end='')
            for astric in range(astrics_number):
                print('*', end='')
            print()
            spaces_number -= 1
            astrics_number += 2
            i += 1


sandglass(2)
print('--------')
sandglass(5)
print('--------')
sandglass(10)
