#!/usr/bin/python3
'''right_pasqual_triangle module'''


def right_pasqual_triangle(size):
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        spaces = size - 1
        astrics = 1
        i = 0

        while i < size:
            for space in range(spaces):
                print(' ', end='')
            for astric in range(astrics):
                print('*', end='')
            print()
            spaces -= 1
            astrics += 1
            i += 1

        spaces = 1
        astrics -= 2
        i -= 1

        while i > 0:
            for space in range(spaces):
                print(' ', end='')
            for astric in range(astrics):
                print('*', end='')
            print()
            spaces += 1
            astrics -= 1
            i -= 1

right_pasqual_triangle(2)
print('----------')
right_pasqual_triangle(5)
print('----------')
right_pasqual_triangle(10)
