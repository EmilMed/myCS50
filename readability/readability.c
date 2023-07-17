#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main(void)
{
    string text = get_string("Text: ");

    int letters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (islower(text[i]))
        {
        letters++;
        }
        else if (isupper(text[i]))
        letters++;
    }
    printf("%i letters\n", i);
}