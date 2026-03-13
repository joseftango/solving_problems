#include <stdio.h>

/**
* subarraySum -  finds a continuous sub-array which adds to a given number 
* @arr: the given array
* @N: length of array
* @S: needle subarray sum 
* Return: left and right index as array or -1
**/

int *subarraySum(int *arr, size_t N, int S)
{
	int i, j, *border, begain = 0, sum = 0;

	for (i = 0; i < N; i++)
	{
		sum = arr[i];

        if (sum == S)
		{
         	border[0] = i + 1;
			return (border);
        }

		for (j = i + 1; j < N; j++)
		{
			begain = i + 1;
			sum += arr[j];

			if(sum == S)
			{
				border[0] = begain;
				border[1] = j + 1;
				return (border);
			}

		}
	}
	printf("no sub array founded");
}



int main(void)
{
int N = 5, S = 12;
int A[] = {1,2,3,7,5};
int *arr_res;

arr_res = subarraySum(A, N, S);

printf("Sum found between position %d and %d\n", arr_res[0], arr_res[1]);


return (0);
}
