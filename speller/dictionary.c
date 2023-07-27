// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 45;

unsigned int sum;
unsigned int i;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    i = hash(word);

    node *cursor = table[i];
    
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned int p = 0;
    for (int j = 0; j < strlen(word); j++)
    {
        p++;
    }
    return p;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }
    char word[LENGTH + 1];

   while (fscanf(file, "%s", word) != EOF)
    {
       fscanf("dictionaries/small", "%s", word);

       if (fscanf() = EOF)
       {
        break;
       }
       node *n = malloc(sizeof(word));
       if (n == NULL)
       {
        return false;
       }
       strcopy(n- >word, word);
       n- > next = table[i];
       table[i] = n;
       sum++;
    }
   fclose(file);
   return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if(sum > 0)
    {
        return sum;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
