#!/usr/bin/python3
'''pyramid module'''


def print_pyramid(size):
    '''function that prints pyramide using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        spaces_number = size - 1
        astrics_number = 1
        i = 0

        while i < size:
            for space in range(spaces_number):
                print(' ', end='')
            for astric in range(astrics_number):
                print('*', end='')
            print()
            spaces_number -= 1
            astrics_number += 2
            i += 1


print_pyramid(2)
print('-------')
print_pyramid(5)
print('-------')
print_pyramid(10)
