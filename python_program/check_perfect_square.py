# Check Perfect Square: Determine if a number is a perfect square. 
import math
def is_perfect_square(number):
    last_digit = [0,1,4,5,6,9]
    unit_digit = number%10
    if number < 0 or unit_digit not in last_digit:
        return False
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

print(f"{is_perfect_square(25)} = ")