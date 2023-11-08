# Check Armstrong Number: Determine if a number is an Armstrong number. 
# 153 -> 1**3 + 5**3 + 3**3 => 153
def check_armstrong(num):
    length = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10
    return True if (sum == num) else False

# number = 153
print(f"{check_armstrong(153) = }")