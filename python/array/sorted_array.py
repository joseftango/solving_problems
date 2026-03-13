#!/usr/bin/python3
'''sort array module'''




def Sort_asc(arr):
    arr_cp = arr[:]
    sorted = []
    for i in range(len(arr)):
        minum = min(arr_cp)
        sorted.append(minum)
        arr_cp.remove(minum)
    return sorted


def Sort_desc(arr):
    arr_cp = arr[:]
    sorted = []
    for i in range(len(arr)):
        maximum = max(arr_cp)
        sorted.append(maximum)
        arr_cp.remove(maximum)
    return sorted


# print(Sort_asc([10, 5, 8, 6, 0]))
# print(Sort_desc([10, 5, 8, 6, 0]))
myl = [24, 55, 78, 64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
print(Sort_asc(myl))
print(Sort_desc(myl))
