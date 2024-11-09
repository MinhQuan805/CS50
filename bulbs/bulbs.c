#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    int array[BITS_IN_BYTE] = {0, 0, 0, 0, 0, 0, 0, 0};
    int m = get_int("");
    int n = 7;
    while (n >= 0)
    {
        int total = pow(2, n);
        if (total <= m)
        {
            m = m - total;
            array[BITS_IN_BYTE - 1 - n] = 1;
        }
        n--;
    }
    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        print_bulb(array[i]);
    }
    printf("\n");

}
void print_bulb(int bit)
{
    if (bit == 0)
    {
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        printf("\U0001F7E1");
    }
}
