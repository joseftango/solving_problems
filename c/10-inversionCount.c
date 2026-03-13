#include <stdio.h>

/**
 * inversionCount - function that finds the inversion Count
 * @arr: the given array
 * Return: inversion Count value
**/

int inversionCount(int *arr, int n)
{
int i, j = 0, inv_count = 0;

for(i = 0; i < n - 1; i++)
	for (j = i + 1; j < n; j++)
	{
		if (arr[j] < arr[i])
			inv_count += 1;
	}
return (inv_count);
}

/**
 * main - testing inversionCount function
 * @void: nothing
 * Return: 0
**/

int main(void)
{
int res = 0, arr1[] = {2, 4, 1, 3, 5}, size1 = sizeof(arr1) / sizeof(arr1[0]);
res = inversionCount(arr1, size1);
printf("%d\n", res);

int arr2[] = {2, 3, 4, 5, 6}, size2 = sizeof(arr2) / sizeof(arr2[0]);
res = inversionCount(arr2, size2);
printf("%d\n", res);

int arr3[] = {3, 2, 4, 6, 5}, size3 = sizeof(arr3) / sizeof(arr3[0]);
res = inversionCount(arr3, size3);
printf("%d\n", res);

return (0);
}
