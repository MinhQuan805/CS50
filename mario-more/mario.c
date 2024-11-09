#include <cs50.h>
#include <stdio.h>
int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            printf(" ");
        }
        for (int k = -1; k < i; k++)
        {
            printf("#");
        }
        for (int m = 0; m < 1; m++)
        {
            printf("  ");
        }
        for (int o = -1; o < i; o++)
        {
            printf("#");
        }

        printf("\n");
    }
}
