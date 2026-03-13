#!/usr/bin/python3
'''left_pasqual_triangle module'''


def left_pasqual_triangle(size):
    '''writes left pasqual triangle using * character'''
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

        astrics_number -= 2
        i -= 1

        while i > 0:
            for astric in range(astrics_number):
                print('*', end='')
            print()
            astrics_number -= 1
            i -= 1


left_pasqual_triangle(2)
print('----------')
left_pasqual_triangle(5)
print('----------')
left_pasqual_triangle(10)
