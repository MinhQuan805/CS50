#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int coleman(string text);

int main(void)
{
    string text = get_string("Text: ");
    int grade = coleman(text);
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}
int coleman(string text)
{
    int l = 0; int s = 0; int w = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            l++;
        }
        if (text[i] == ' ')
        {
            w++;
        }
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            s++;
        }
    }
    float index = 0.0588 * (l / (float) w) * 100 - 0.296 * (s / (float) w) * 100 - 15.8;
    return round(index);
}
