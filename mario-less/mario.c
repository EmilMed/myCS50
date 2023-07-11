#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n > 8 || n < 1);

    for (int g = 1; g < n + 1; g++)
    {
        for (int i = g; i > 1; i--)
        {
            printf(".");
        }
        for (int o = 0; o < i; o++)
        {
            printf("#\n");
        }
        printf("\n");
        break
    }

}