#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
 if(argc != 2)
 {
    printf("Usage: ./recover IMAGE\n");
    return 1;
 }

 FILE *f = fopen(argv[1], "r");
 if (f == NULL)
 {
    printf("Could not open file.");
    return 2;
 }

  unsigned char buffer[512];

  int JPEG_counter = 0;

  FILE *output = NULL;

  char *filename = malloc(8 * sizeof(char));

 for(i = 0; i < memory card length; i++)
 {
    while (fread(buffer, 512 , 1, f))
    if(buffer[0] = 0xff && buffer[1] = 0xd8 && buffer[2] = 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        sprintf
        JPEG_counter++
        if (JPEG_counter = 1)
        {

        }
    }
 }
}

