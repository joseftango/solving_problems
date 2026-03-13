#include <stdio.h>

/**
 * allPairs - finds all pairs from both arrays whose sum is equal to X
 * @a1: first array
 * @a2: second array
 * @x: the required sum
 * @size1: size of a1
 * @size2: size of a2
 * Return: returns the sorted vector pair values of all the pairs
**/

void allPairs(int *a1, int *a2, int size1, int size2, int x)
{
int i, j;
for (i = 0; i < size1; i++)
{
	for (j = 0; j < size2; j++)
		if ((a1[i] + a2[j]) == x)
			printf("(%d, %d)\n", a1[i], a2[j]);
}
}

/**
 * main - testing allPairs function
 * @void: nothing
 * Return: 0
 * **/


int main(void)
{
	int arr1[] = {-1, -2, 4, -6, 5, 7};
	int arr2[] = {6, 3, 4, 0};
	int n = sizeof(arr1) / sizeof(int);
	int m = sizeof(arr2) / sizeof(int);
	int x = 8;
	allPairs(arr1, arr2, n, m, x);




	return (0);
}
