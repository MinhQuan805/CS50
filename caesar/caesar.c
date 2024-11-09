#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char list[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
bool only_digit(string key, int argc);
string rotate(string key);
char formula(char t, int k);

int main(int argc, string argv[])
{
    if (only_digit(argv[1], argc))
    {
        string cipher = rotate(argv[1]);
        printf("ciphertext: %s\n", cipher);
        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
bool only_digit(string key, int argc)
{
    if (argc == 2)
    {
        for (int j = 0, m = strlen(key); j < m; j++)
        {
            if (!isdigit(key[j]))
            {
                return false;
            }
        }
        return true;
    }
    else
    {
        return false;
    }
}
string rotate(string mykey)
{
    int key = atoi(mykey);
    string plain = get_string("plaintext: ");
    for (int i = 0, n = strlen(plain); i < n; i++)
    {
        if (isalpha(plain[i]))
        {
            if (isupper(plain[i]))
            {
                // Khá thừa
                char text = tolower(plain[i]);
                char newtext = formula(text, key);
                plain[i] = toupper(newtext);
            }
            else if (islower(plain[i]))
            {
                plain[i] = formula(plain[i], key);
            }
        }
    }
    return plain;
}
char formula(char t, int k)
// không cần phải chia ra k < 26 hay k > 26 vì % tự động lấy phần dư thuộc list[]
{
    char result = list[(t - 'a' + k) % 26];
    return result;
}
