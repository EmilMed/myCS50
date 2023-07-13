#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;
do
  {
      n = get_int("Start size:20 ");
  }
  while (n < 9);
    // TODO: Prompt for end size
    int x;
do
  {
    x = get_int("End size: ");
  }
  while (x < n);
    // TODO: Calculate number of years until we reach threshold
     int y;
    y = (x - n) / ((n / 3) - (n / 4));
    // TODO: Print number of years
    printf("Years: %i\n", y);
}
