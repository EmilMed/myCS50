// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

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
unsigned int hash_value;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    hash_value = hash(word);

    node *cursor = table[hash_value];

    while(cursor != 0)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
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
       node *n = malloc(sizeof(word));

       if (n == NULL)
       {
        return false;
       }

       strcpy(n->word, word);
       n-> next = table[hash_value];
       table[hash_value] = n;
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
    for(int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            tmp = cursor;
            free(tmp);
        }
        if (cursor == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
