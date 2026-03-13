#include <stdio.h>

/**
 * reverseInGroups - Reverse every sub-array group of size K
 * @arr: given array
 * @n: lenght of the given array
 * @k: lenght of sub-array
 * Return: nothing
**/

void reverseInGroups(int *arr, int n, int k)
{
int i, j = 0, tmp = 0;

for (i = 0; i < k / 2; i++)
{
	tmp = arr[i];
	arr[i] = arr[k - i - 1];
	arr[k - i - 1] = tmp;
}

for (j = k; j < (n + j) / 2; j++)
{
	tmp = arr[j];
	arr[j] = arr[n - 1];
	arr[n - 1] = tmp;

}
}

/**
 * main - function that call reverseInGroups to test it
 * @void: no argument given
 * Return: 0
**/

int main(void)
{

int arr1[] = {1, 2, 3, 4, 5}, N = 5, K = 3, i;
int arr2[] = {5, 6, 8, 9}, N2 = 4, K2 = 3;

reverseInGroups(arr1, N, K);


for (i = 0; i < N; i++)
	printf("%d   ", arr1[i]);


printf("\n");

reverseInGroups(arr2, N2, K2);

for (i = 0; i < N2; i++)
	printf("%d   ", arr2[i]);


return (0);
}
