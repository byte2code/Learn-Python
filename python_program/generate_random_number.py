# Generate Random Number: Generate a random number within a specified 
# range.
import random
def generate_random_number(low, high):
    return random.randint(low, high)

print(f"{generate_random_number(50, 120) = }")