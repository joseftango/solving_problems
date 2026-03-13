#!/usr/bin/python3


def rearrange(a, n):
    '''rearrange the array elements alternatively'''
    output = []
    i = 0
    j = n - 1

    while i < j:
        output.append(a[j])
        output.append(a[i])

        j = j - 1
        i = i + 1

    if i == j:
        output.append(a[i])

    for i in range(len(output)):
        print(output[i], end="  ")
    print()


#------------------------ try function -----------------------------#


arr1 = [1,2,3,4,5,6]
l1 = len(arr1)
rearrange(arr1, l1)


arr2 = [10,20,30,40,50,60,70,80,90,100,110]
l2 = len(arr2)
rearrange(arr2, l2)

