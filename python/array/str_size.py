#!/usr/bin/python3
'''str_size module'''


def str_size(string):
    '''find the number of words in given sentence'''
    count = 0   
    for i in range(len(string)):
        if i == len(string) - 1:
            count += 1
        if string[i] in ' ':
            count += 1
    return count


print(str_size('I am having a very nice day.'))
