#!/usr/bin/python3
'''diamond module'''


def diamond(size):
    '''prints diamond form using * character'''
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

        spaces_number = 1
        astrics_number -= 4
        i -= 1

        while i > 0:
            for space in range(spaces_number):
                print(' ', end='')
            for astric in range(astrics_number):
                print('*', end='')
            print()
            spaces_number += 1
            astrics_number -= 2
            i -= 1



diamond(2)
print('--------')
diamond(5)
print('--------')
diamond(10)
