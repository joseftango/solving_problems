#!/usr/bin/python3
'''double_hill module'''


def double_hill(size):
    '''draw a double hill using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        spaces = size - 1
        astrics = 1
        spaces_between = (size * 2) - 3
        i = 0

        while i < size:
            for space in range(spaces):
                print(' ', end='')
            for astric in range(astrics):
                print('*', end='')
            for space in range(spaces_between):
                print(' ', end='')
            if i == size - 1:
                astrics -= 1
            for astric in range(astrics):
                print('*', end='')

            print()
            spaces -= 1
            spaces_between -= 2
            astrics += 2
            i += 1




double_hill(5)
