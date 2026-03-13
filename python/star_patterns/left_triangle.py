#!/usr/bin/python3
'''left_triangle module'''

def left_triangle(size):
    '''function that writes a left triangle using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        i = 0
        astrics_number = 1
        while i < size:
            for astric in range(astrics_number):
                print('*', end='')
            print()
            astrics_number += 1
            i += 1

left_triangle(5)
print('---------')
left_triangle(10)
print('---------')
left_triangle(2)
