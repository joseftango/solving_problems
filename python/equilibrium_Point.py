#!/usr/bin/python3
def equilibriumPoint(arr):
	"""function that finds equilibrium
	point in a given array"""
	if len(arr) == 0:
		return -1

	if (len(arr) == 1):
		return arr[0]

	for i in range(len(arr)):	
		sum_before = 0
		sum_after = 0

		for x in range(i):
			sum_before += arr[x]

		for j in range(i + 1, len(arr)):
			sum_after += arr[j]

		if sum_before == sum_after:
			return arr[i]
	return -1


A = [1, 3, 5, 2, 2]
res = equilibriumPoint(A)
print(res)

A1 = [1]
res = equilibriumPoint(A1)
print(res)

A2 = [2, 2, 2, 10, 6]
res = equilibriumPoint(A2)
print(res)
