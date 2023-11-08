# Factorial Using Recursion: Calculate the factorial of a number using 
# recursion. 
def factorial_recursion(num):
    if num == 0 or num == 1:
        return 1
    res = num
    for i in range(1, num):
        res *= i
    return res

print(f"{factorial_recursion(6) = }")