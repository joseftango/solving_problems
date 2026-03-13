#!/usr/bin/python3


def kthElement(arr1, arr2, k):
	"""function that rearrange two arrays"""
	new_arr = []
	n = len(arr1)
	m = len(arr2)

	for i in range(n):
		new_arr.append(arr1[i])
	for j in range(m):
		new_arr.append(arr2[j])
	sorted_new_arr = sorted(new_arr)

	for i in range(n + m):
		print(sorted_new_arr[i], end=" ")
		if i == k - 1:
			needed_num = sorted_new_arr[i]
	print()

	return needed_num

#-----------------------------trying function--------------------------------#

arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
kth = 5

res = kthElement(arr1, arr2, kth)
print(res)

arr3 = [100, 112, 256, 349, 770]
arr4 = [72, 86, 113, 119, 265, 445, 892]
kth = 7

res = kthElement(arr3, arr4, kth)
print(res)
