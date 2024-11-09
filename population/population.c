#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int s;
    int e;
    do
    {
        s = get_int("Start size: ");
    }
    while (s < 9);
    do
    {
        e = get_int("End size: ");
    }
    while (s > e);
    int count = 0;
    for (;s < e; s = s + (s/3) - (s/4))
    {
        count ++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", count);
}
