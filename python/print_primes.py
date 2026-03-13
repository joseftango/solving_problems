#!/usr/bin/python3
'''primes module'''


def prime_nums():
    '''prints prime numbers between 100 - 200'''
    n = 100
    l = []
    while n <= 200:
        for x in range(2, (n // 2) + 1):
            # if n > 200:
            #     return None
            if n % x == 0:
                n += 1
                x = 2
                
        # if n == 199:
        #     print(n, end='')
        # else:
            # print(n, end=', ')
        l.append(n)
        n += 1
    return l

l1 = []
for num in range(100, 200):
    if all(num % i != 0 for i in range(2, num)):
        l1.append(num)

print(prime_nums())
print(l1)
