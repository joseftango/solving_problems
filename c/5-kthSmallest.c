#include <stdio.h>

/**
 * swap - function that switch two integer
 * @x: first integer
 * @y: second integer
 * Return: nothing
**/

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

/**
 * bubbleSort - arrange array in ascending order
 * @arr: given array
 * @n: size of the array
 * Return: nothing
**/

void bubbleSort(int arr[], int n)
{
	int i, j;

	for (i = 0; i < n - 1; i++)
		for (j = 0; j < n - i - 1; j++)
			if (arr[j] > arr[j + 1])
				swap(&arr[j], &arr[j + 1]);
}

/**
 * kthSmallest - finds the kth smallest integer in array
 * @arr: the given array
 * @size: size of the array
 * @k: integer
 * Return: the kth smallest integer
**/

int kthSmallest(int *arr, int size, int k)
{
	if (size == 0)
		return (0);

	bubbleSort(arr, size);

	return (arr[k - 1]);
}

/**
 * main - testing three functions
 * @void: no given arguments
 * Return: 0
**/

int main(void)
{

int arr[] = {7, 10, 4, 3, 20, 15}, N = 6, K = 3, res = 0;
int arr1[] = {7, 10, 4, 20, 15};

res = kthSmallest(arr, N, K);
printf("%d\n", res);

N = 5, K = 4;

res = kthSmallest(arr1, N, K);
printf("%d\n", res);



return (0);
}
