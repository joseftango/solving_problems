#include <stdio.h>
#include <limits.h>

/**
 * maxSubarraySum - Finds the sub-array which has the maximum sum
 * @arr: the given array
 * @n: size of the array
 * Return: sub-array that has the maximum sum
 * **/



int maxSubarraySum(int *arr, int n)
{
int start_index, sum, i = 0, subarray_size = 0, ans = INT_MIN;

for (subarray_size = 1; subarray_size <= n; subarray_size++)
{
	for (start_index = 0; start_index < n; start_index++)
	{
		if (start_index + subarray_size > n)
			break;

		sum = 0;
		for (i = start_index; i < start_index + subarray_size; i++)
			sum += arr[i];

		if (sum > ans)
			ans = sum;
	}
}
	return (ans);
}

/**
 * main - testing maxSubarraySum function
 * @void: nothing
 * Return: 0
**/


int main(void)
{

int Arr[] = {1, 2, 3, -2, 5}, Arr1[] = {-1, -2, -3, -4}, N = 5, res = 0;


res = maxSubarraySum(Arr, N);
printf("%d\n", res);

N = 4;

res = maxSubarraySum(Arr1, N);
printf("%d\n", res);



return (0);
}
