#!/usr/bin/python3
'''fibonacci_series module'''



def fibo(n):
    '''prints fibonacci numbers'''
    if n <= 0:
        return -1
    curr = 0
    i = 2
    a = 0
    b = 1
    print(a, end=', ')
    print(b, end=', ')

    while i < n:
        curr = a + b
        if i == n - 1:
            print(curr)
        else:
            print(curr, end=', ')
        a = b
        b = curr
        i += 1


fibo(5)
fibo(10)
fibo(12)