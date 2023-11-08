# Print Fibonacci sequence:
def fibonacci(num):
    a, b = 0, 1
    print(a, b, end=" ")
    for i in range(num):
        a, b = b, a+b
        print(b, end=" ")

print(f"{fibonacci(5) = }")