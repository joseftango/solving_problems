#include <stdio.h>

/**
 * maxLen - computes length of the largest subarray with sum 0
 * @arr: the given array
 * n: size of the array
 * Return: size of largest subarray with sum 0
**/

int maxLen(int *arr, size_t n)
{
int i,j, length = 1, sum = 0, subarr = 0;

    if (arr == NULL)
        return (0);
    
    for (i=0; i < n; i++) 
        {
        sum = arr[i];
        length = 1;

        for (j = i + 1; j < n; j++)
        {
            sum += arr[j];
            length++;

            if (sum == 0 && length > subarr)
                subarr = length;
        }
        }
        if (subarr == 0)
            return (-1);

    return (subarr);
}


/**
* main - function that tests maxLen
* @void: nothing
* Return: 0
**/


int main(void)
{
size_t N = 8;
int A[] = {15,-2,2,-8,1,7,10,23};
int res = 0;

res = maxLen(A, N);
printf("%d\n", res);


return 0;
}
