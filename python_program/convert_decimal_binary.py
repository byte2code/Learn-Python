# Convert Decimal to Binary: Convert a decimal number to binary. 
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2

    return binary_num

decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(f"Binary of {decimal_number}: {binary_number}")