from cs50 import get_int

def main():
  x = get_height()
  for i in range(x):
    for j in range(x):
      if (i + j >= x - 1):
        print("#", end="")
      else:
        print(" ", end="")
    print()

def get_height():
   while True:
    n = get_int("Height: ")
    if n < 9 and n > 0:
      return n

main()

