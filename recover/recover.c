#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

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

  FILE *outputf = NULL;

  char *filename = malloc(8 * sizeof(char));

  while (fread(buffer, sizeof(char) , 512, f))
    {
      if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        sprintf(filename, "%03i.jpg", JPEG_counter);

        outputf = fopen(filename, "w");

        JPEG_counter++;
    }
      if (outputf != NULL)
        {
          fwrite(buffer, sizeof(char), 512, outputf);
        }
    }
    
    free(filename);
    fclose(outputf);
    fclose(f);

    return 0;
}

