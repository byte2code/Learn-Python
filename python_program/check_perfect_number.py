# Check Perfect Number: Determine if a  number is a perfect number.

def check_perfect_number(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return True if sum(factors) == num else False

print(f"{check_perfect_number(28) = }")