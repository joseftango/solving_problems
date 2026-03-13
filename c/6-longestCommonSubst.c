#include <stdio.h>

/**
* longestCommonSubst - searchs the lenght of longest comman subarray
* @S1: first string
* @S2: second string
* @m: length of S1
* @n: length of S2
* Return: length of the longest comman subarray or 0
**/


int longestCommonSubst(char *S1, char *S2, int m, int n)
{
int i,j, count = 0, longest = 0;

	if (!S1 || !S2)
		return (-1);

	for (i = 0; i < m; i++)
	{
		for  (j = 0; j < n; j++)
		{
			if (S1[i] == S2[j])
			{
				count++;
				i++;
			}

		}

		if (count > longest)
		{
			longest = count;
			count = 0;	
		}

	}

	return (longest);
}




int main(void)
{

char *str1 = "ABCDGH";
char *str2 = "ACDGHR";

int l1 = 6;
int l2 = 6;
int res = 0;



res = longestCommonSubst(str1, str2, l1, l2);

printf("%d\n", res);

str1 = "OldSite:GeeksforGeeks.org";
str2 = "NewSite:GeeksQuiz.com";
l1 = 9;
l2 = 9;

res = longestCommonSubst(str1, str2, l1, l2);

printf("%d\n", res);




return (0);

}