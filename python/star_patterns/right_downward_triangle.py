#!/usr/bin/python3
'''right_downward_triangle module'''


def right_downward_triangle(size):
    '''print right downward triangle using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        astrics_number = size
        i = 0

        while i < size:
            for astric in range(astrics_number):
                print('*', end='')
            print()
            astrics_number -= 1
            i += 1

right_downward_triangle(2)
print('---------')
right_downward_triangle(5)
print('---------')
right_downward_triangle(10)
