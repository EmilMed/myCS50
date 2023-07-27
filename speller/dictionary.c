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

unsigned int word_count;
unsigned int i;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int j = 0; j < N - 1; j++)
    {
        if(strlen(word) = 0)
        {
            return 1;
        }
        else if (strlen(word) = 1)
        {
            int 0 = hash(word)
        }
        sum++;
    }
    return toupper(word[0]) - 'A';
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
       word_count++;
    }
   return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
