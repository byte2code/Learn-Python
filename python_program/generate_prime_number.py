# Generate Prime Numbers: Generate and print prime numbers within a 
# given range. 

def generate_prime(num):
    if num <= 1:
        print("Prime doesn't exist")
        return
    primes = []
    # lambda
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
            if i not in primes:
                primes.append(i)
    return primes

print(f"{generate_prime(20) = }")