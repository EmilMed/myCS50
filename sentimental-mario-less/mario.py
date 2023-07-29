from cs50 import get_int


def main():
  height = get_height()
  for i in range(height):
    for j in range(height):
      if (i + j) > (n - 2):
        print("#")
      else:
        print(" ")
  print("\n")

def get_height():
   while True:
    n = get_int("Height: ")
    if n < 9 and n > 0:
      return n
    
main()

