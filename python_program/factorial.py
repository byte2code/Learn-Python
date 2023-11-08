# Calculate the factorial (Recursion). 
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

print(f"{factorial(5) = }")