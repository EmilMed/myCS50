#include <cs50.h>
#include <stdio.h>

int main(void)
{ // Obtain positive integer in range between 1 and 8
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n > 8 || n < 1);
// For EACH ROW
    for (int g = 1; g < n + 1; g++)
    { // DOTS
        for (int i = n - 1; i > 1; i--)
        {
            printf(".");
        } // HASHES
           for (int o = 1; o < n; o++)
        {
            printf("#");
        }
        printf("\n");
        break;
    }

}