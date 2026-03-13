#!/usr/bin/python3
'''butterfly module'''


def butterfly(size):
    '''print butterfly form using * character'''
    if type(size) is not int:
        raise TypeError('size must be a number')
    elif size <= 1:
        raise ValueError('size must be greater than 1 and 2 minimum')
    else:
        astrics = 1
        spaces_between = (size * 2) - 3
        i = 0

        while i < size:
            for astric in range(astrics):
                print('*', end='')
            for space in range(spaces_between):
                print(' ', end='')
            if i == size - 1:
                astrics -= 1
            for astric in range(astrics):
                print('*', end='')
            print()
            astrics += 1
            spaces_between -= 2
            i += 1

        astrics = size - 1
        spaces_between = 1

        while i > 0:
            for astric in range(astrics):
                print('*', end='')
            for space in range(spaces_between):
                print(' ', end='')
            for astric in range(astrics):
                print('*', end='')
            print()

            astrics -= 1
            spaces_between += 2
            i -= 1



butterfly(2)
print('--------')
butterfly(5)
print('--------')
butterfly(10)
print('--------')
butterfly(4)
print('--------')
