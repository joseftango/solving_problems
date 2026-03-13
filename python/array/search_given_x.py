#!/usr/bin/python3
'''search_given_x module'''


def search_given_x(arr, x):
    '''search element in array'''
    if arr == None or arr == []:
        return -1
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

l = [2, 5, 6, 7, 3, 0, 8, 2]

print(search_given_x(l, 8))
