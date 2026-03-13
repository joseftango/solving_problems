#include <stdio.h>
#include <stdlib.h>

/**
* isPowerofTwo - function that checks whether N is a power of 2
* @N: non negative integer
* Return: 1 or 0, -1 if fail
**/

int isPowerofTwo(unsigned int N)
{
	int check_in = 0;
	int i = 0;

	if (N == 0)
	{
		printf("%d pow 2 = %d\n", N, N * N);
		return (1);
	}

	for (i = 0; i <= N; i++)
	{
		check_in = i * i;

		if (check_in == N)
		{
			printf("%d pow 2 = %d\n", i, check_in);
			return (1);
		}

		if (check_in > N)
			return (0);
	}

	return (-1);
}

/**
* main - function that call is isPowerofTwo function to run it
* @argc: number of argument passed
* @argv: double pointer to string
* Return: 0
* **/

int main(int argc, char *argv[])
{
int res = 0;
int x = atoi(argv[1]);

res = isPowerofTwo(x);
printf("%d\n", res);

return (0);
}
