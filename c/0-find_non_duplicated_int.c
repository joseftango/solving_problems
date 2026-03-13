#include <stdio.h>
/**
* firstNonRepeating - function that finds a non duplicated integer
* @arr: array of integer
* @n: the lenght of the given array
* Return: int 
**/

int firstNonRepeating(int arr[], int n)
{
    int j, i;

    for (int i = 0; i < n; i++)
	{
        for (j = 0; j < n; j++)
            if (i != j && arr[i] == arr[j])
                break;

        if (j == n)
            return arr[i];
    }
    return (-1);
}



int main()
{
	int res = 0;
    int arr[] = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    res = firstNonRepeating(arr, n);
	printf("%d\n", res);


    return 0;
}
