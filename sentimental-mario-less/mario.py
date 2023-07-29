from cs50 import get_int

def get_height():
   while True:
    n = get_int("Height: ")
    if n > 8 and n < 1:
      break
   return n

def main():
  height = get_height()
  for i in range(height):
    for j in range(height):
      if (i + j) > (n - 2):
        print("#")
      else:
        print(" ")
  print("\n")

main()

