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
    for (int g = 0; g < n; g++)
     { // For EACH COLUMN
        for (int h = 0; h < n; h++)
          { if (g + h > n - 2)
              printf("#");
           else
              printf(" ");
          }
     printf("\n");
  }
}
