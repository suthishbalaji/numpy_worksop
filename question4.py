#write a program to find the sum of digits of a given number'
def sum_of_digits(number):
    number = abs(number)
    total_sum = 0
    while number > 0:
        total_sum += number % 10
        number //= 10
    return total_sum
number = int(input("Enter a number: "))
print("The sum of the digits is:", sum_of_digits(number))
