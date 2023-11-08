# Check Prime Number: Determine if a number is prime or not. 
def check_prime(num):
    if num <= 1:
        return False    
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True

print(f"{check_prime(15) = }")
print(f"{check_prime(13) = }")