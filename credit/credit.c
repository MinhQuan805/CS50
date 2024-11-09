#include <cs50.h>
#include <stdio.h>
#include <string.h>

int condition(long n);
bool check(int x);
void name_of_credit(long me);

int main(void)
{
    long n = get_long("Number: ");
    int z = condition(n);
    if (check(z))
    {
        name_of_credit(n);
    }
    else
    {
        printf("INVALID\n");
    }
}

int condition(long n)
{
    int m = 0; int sum1 = 0; int sum2 = 0;
    while (n > 0)
    {
        int i = n % 10;
        n = n / 10;
        m++;
        if (m % 2 == 0)
        {
            int newi = 2 * i;
            if (newi > 9)
            {
                while (newi > 0)
                {
                    int breaki = newi % 10;
                    newi = newi / 10;
                    sum1 += breaki;
                }
            }
            else
            {sum1 += newi;}
        }
        else
        {sum2 += i;}
    }
    return sum1 + sum2;
}
bool check(int x)
{
    if (x % 10 == 0){
        return true;
    }
    else {
        return false;
    }
}
void name_of_credit(long me)
{
    char str[20];
    sprintf(str, "%ld", me);
    int len = strlen(str);
    if ((len == 13 || len == 16) && str[0] == '4')
    {
        printf("VISA\n");
    }
    else if (len == 16 && str[0] == '5' && str[1] >= '1' && str[1] <= '5')
    {
        printf("MASTERCARD\n");
    }
    else if (len == 15 && str[0] == '3' && (str[1] == '4' || str[1] == '7'))
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

