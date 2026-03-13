#!/usr/bin/python3
'''right_triangle module'''


def right_triangle(size):
    '''function that writes a right triangle using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        spaces = size - 1
        astrics = 1
        i = 0
        while(i < size):
            for space in range(spaces):
                print(' ', end='')
            for astric in range(astrics):
                print('*', end='')
            print()
            spaces -= 1
            astrics += 1
            i += 1

right_triangle(2)
print('------------')
right_triangle(5)
print('------------')
right_triangle(10)
