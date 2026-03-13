#!/usr/bin/python3
''' palindrome_str module'''


def Palindrome_str(string):
    '''checks if string is palinfrome or not'''
    rev_str = string[::-1]
    if string == rev_str:
        return True
    return False



print(Palindrome_str('ttstt'))
print(Palindrome_str('tttts'))
