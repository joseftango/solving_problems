#include <stdio.h>

/**
 * trappingWater - counts how much water trapped between the blocks
 * @arr: the given array
 * @n: size of the array
 * Return: number of blocks taken by water
**/

int trappingWater(int *arr, int n)
{
int i = 0, global_area = 0, taken_area = 0, border = 0,  water = 0;

if (n == 0)
	return (-1);

if (arr[0] < arr[n - 1])
	border = arr[0];
else
	border = arr[n - 1];

global_area = (border * n);

	for (i = 1; i < n - 1; i++)
		taken_area += arr[i];

water = (global_area - taken_area) - (border * 2);

	if (water < 0)
		return (0);

	return (water);
}

/**
 * main - testing trappingWater
 * @void: nothing
 * Return: 0
**/

int main(void)
{
int res = 0, arr1[] = {3, 0, 0, 2, 0, 4}, N1 = 6;

res = trappingWater(arr1, N1);
printf("%d\n", res);

int arr2[] = {5, 8, 0, 2, 7, 6}, N2 = 6;
res = trappingWater(arr2, N2);
printf("%d\n", res);

int arr3[] = {7, 4, 0, 9}, N3 = 4;
res = trappingWater(arr3, N3);
printf("%d\n", res);


return (0);
}
