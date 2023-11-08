# Calculate GCD: Calculate the greatest common divisor (GCD) of two 
# numbers.

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


input_values = (14, 1400)
result = calculate_gcd(*input_values)

print(f"GCD for calculate_gcd{input_values} = {result}")

