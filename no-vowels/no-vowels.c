
#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string s);
int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("%s\n", replace(argv[1]));
    }
    else
    {
        printf("Usage: ./no-vowels word\n");
    }
}
string replace(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        switch (s[i])
        {
            case 'a':
                s[i] = '6';
                break;
            case 'e':
                s[i] = '3';
                break;
            case 'i':
                s[i] = '1';
                break;
            case 'o':
                s[i] = '0';
                break;
            default:
                s[i] = s[i];
                break;
        }
    }
    return s;
}
