#include <cs50.h>
#include <stdio.h>
// Cách này cũng okk nhưng mà mình sẽ không biết được có bao nhiêu quarter, hay dimes, hay nickels..
int main(void)
{
    int n;
    do
    {
        n = get_int("Change Owed: ");
    }
    while (n < 0);
    int count = 0;
    while (n > 0)
    {
        if (n >= 25)
        {
            n = n - 25;
            count ++;
        }
        else if (n >= 10)
        {
            n = n - 10;
            count ++;
        }
        else if (n >= 5)
        {
            n = n - 5;
            count ++;
        }
        else
        {
            n = n - 1;
            count ++;
        }
    }
    printf("%i\n", count);
}
