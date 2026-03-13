#!/usr/bin/python3
'''largest range module'''


def largest_range(array):
    '''returns an array of two length contained
    the largest range number of array'''
    return [array[0], array[len(array) - 1]]


print(largest_range([2, 3, 4, 5, 6]))