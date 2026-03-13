#include <stdio.h>
#include <stdlib.h>

/**
* set the Kth bit - sets the Kth bit in the binary representation of N 
* @N: given number
* @K: the kth bit
* Return: the transformed integer after changing the kth bit
**/

int setKthBit(unsigned int N, int K)
{
	int bit_status = 0;

	if (K > 64)
		return (-1);

	bit_status = ((1 << K) | N);

	return (bit_status);
}

/**
* main - function used to run setKthBit to work in it
* Return: 0
**/


int main(void)
{
	int res = 0, num = 10, index = 2;

	res = setKthBit(num, index);
	printf("%d\n", res);

	num = 15, index = 3;

	res = setKthBit(num, index);
	printf("%d\n", res);


	return(0);
}
