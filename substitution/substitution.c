#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string convert(string plain, string list);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    string key = argv[1];
    if (strlen(key) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }
    for (int i = 0, n = strlen(key); i < n; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must contain alphabet\n");
            return 1;
        }
        for (int j = 0; j < i; j++)
        {
            if (tolower(key[i]) == tolower(key[j]))
            {
                printf("Key can not be duplicate\n");
                return 1;
            }
        }
    }
    string plain = get_string("plaintext: ");
    string cipher = convert(plain, key);
    printf("ciphertext: %s\n", cipher);
    return 0;
}

string convert(string plain, string list)
{
    for (int k = 0, m = strlen(plain); k < m; k++)
    {
        if (isalpha(plain[k]))
        {
            if (isupper(plain[k]))
            {
                char result = list[plain[k] - 65];
                plain[k] = toupper(result);
            }
            else if (islower(plain[k]))
            {
                char result = list[plain[k] - 97];
                plain[k] = tolower(result);
            }
        }
    }
    return plain;
}
