# Check a Number is Positive, Negative, or Zero: Determine if a number is positive, negative, or zero.

def check_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(f"{check_number_sign(5) = }")
print(f"{check_number_sign(0) = }")
print(f"{check_number_sign(-15) = }")