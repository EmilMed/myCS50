from cs50 import get_string
from math import round
from stdio import isalpha

text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

for i in range(len(text)):
    if isalpha(text[i]):
        letters += 1
    elif text[i] == " ":
        words += 1
    elif text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences += 1
