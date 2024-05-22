# find if the given number is a palindrome or not?
num = int(input())
rev = str(num)
rev = num[::-1]
if ( num == rev):
  print("It is palindrome")
else:
  print("It is not palindrome")
