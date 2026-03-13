#!/usr/bin/python3
'''left_downward_triangle module'''


def left_downward_triangle(size):
    '''print left downward triangle using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        spaces = 0
        astrics = size
        i = size

        while i > 0:
            for space in range(spaces):
                print(' ', end='')
            for astric in range(astrics):
                print('*', end='')
            print()
            spaces += 1
            astrics -= 1
            i -= 1


left_downward_triangle(2)
print('--------')
left_downward_triangle(5)
print('--------')
left_downward_triangle(10)
