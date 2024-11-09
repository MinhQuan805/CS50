#include <cs50.h>
#include <stdio.h>
int calculate_quarters(int n);
int calculate_dimes(int n);
int calculate_nickels(int n);
int calculate_pennies(int n);
int main(void)
{
    int n;
    do
    {
        n = get_int("Change Owed: ");
    }
    while (n < 0);
    int quarters = calculate_quarters(n);
    n = n - (quarters * 25);
    int dimes = calculate_dimes(n);
    n = n - (dimes * 10);
    int nickels = calculate_nickels(n);
    n = n - (nickels * 5);
    int pennies = calculate_pennies(n);
    n = n - (pennies * 5);
    int lap = quarters + dimes + nickels + pennies;
    printf("%i\n", lap);
}
int calculate_quarters(int n)
{
    int quarters = 0;
    while (n >= 25)
    {
        quarters++;
        n = n - 25;
    }
    return quarters;
}
int calculate_dimes(int n)
{
    int dimes = 0;
    while (n >= 10)
    {
        dimes++;
        n = n - 10;
    }
    return dimes;
}
int calculate_nickels(int n)
{
    int nickels = 0;
    while (n >= 5)
    {
        nickels++;
        n = n - 5;
    }
    return nickels;
}
int calculate_pennies(int n)
{
    int pennies = 0;
    while (n > 0)
    {
        pennies++;
        n = n - 1;
    }
    return pennies;
}
