// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>

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
    int sum = LENGTH;
    for (int j = 0; j < N - 1; j++)
    {

    }
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    if (dictionary == NULL)
    {
        return false;
    }
    FILE *file = fopen("dictionaries/small", "r");

    for(int i = 0; i < LENGTH + 1; i++)
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
       hash[i] = word;
       n- > word = i;
       n = i;
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
