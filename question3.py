#write a program to find the factorial of a nummber
def factorial(n):
  if (n == 0 || n == 1):
    return 1
  else:
    return n * factorial(n-1)

n = 5
factorial (5)
