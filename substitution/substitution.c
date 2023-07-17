#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[])
{
  if (argc != 2)
  {
    printf("Usage: ./substitution key\n");
    return 1;
  }
  string key = argv[1];
  for(i = 0; i < strlen(key); i++)
  {
    if (!isalpha(key[i]))
    {
    printf("Usage: ./substitution key\n");
    return 1;
    }
  }
  if (strlen(key) != 26)
  {
    printf("The key must contain 26 characters.\n");
    return 1;
  }
  for(i = 0; i < strlen(key); i++)
  {
    for(j = i + 1; j < strlen(key); j++)
    {
      if(toupper(key[i]) == toupper(key[j])
      {
        printf("Usage: ./substitution key\n");
        return 1;
      }
    }
  }
   string plaintext = get_string("Plaintext: ");

   for(i = 0; i < strlen(key); i++)
   {
    if(islower(key[i]))
    {
      key[i] = key[i] - 32;
    }
   }
   
}