from cs50 import get_int


def main():
  n = get_height()
  for i in range(0, n, 1):
    for j in range(0, n, 1):
      if (i + j > n - 1):
        print("#")
      else:
        print(" ", end="")
  print()

def get_height():
   while True:
    n = get_int("Height: ")
    if n < 9 and n > 0:
      break
    
main()

