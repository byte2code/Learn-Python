# Calculate LCM: Calculate the least common multiple (LCM) of two numbers. 

def calculate_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    greater = a if a > b else b 

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm
    # return (a * b) // calculate_gcd(a,b)

input_values = (14, 1400)
result = calculate_lcm(*input_values)

print(f"LCM for calculate_lcm{input_values} = {result}")
