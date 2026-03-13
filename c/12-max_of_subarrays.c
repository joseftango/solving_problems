#include <stdio.h>

/**
 * max_of_subarrays - Finds the maximum for each and every subarray
 * @arr: the given array
 * @n: length
 * @k: subarray length
 * Return: void
**/

void max_of_subarrays(int *arr, int n, int k)
{
int i, j = 0, max;

for (i = 0; i <= n - k; i++)
{
	max = arr[i];
	for (j = 1; j < k; j++)
	{
		if (arr[i + j] > max)
			max = arr[i + j];
	}
	printf("%d ", max);
}
printf("\n");
}

/**
 * main - testing max_of_subarrays function
 * @void: nothing
 * Return: 0
**/

int main(void)
{

int A[] = {1, 2, 3, 1, 4, 5, 2, 3, 6};
int N = 9, K = 3;

max_of_subarrays(A, N, K);

int A1[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13};
N = 10, K = 4;

max_of_subarrays(A1, N, K);


return (0);
}
