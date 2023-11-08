# Generate a List of Primes: Generate a list of prime numbers up to a specified limit using the Sieve of Eratosthenes. 

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    primes = []

    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False

    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)

    return primes

limit = 50
prime_list = sieve_of_eratosthenes(limit)
print("List of prime numbers up to", limit, ":", end= " ")
print(prime_list)