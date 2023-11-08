def binary_to_decimal(binary_num):
    decimal_num = 0
    # binary_num = binary_num[::-1]
    binary_length = len(binary_num)

    for i in range(binary_length):
        if binary_num[binary_length - i - 1] == '1':
            decimal_num += 2 ** i

    return decimal_num

binary_number = "101010"
decimal_number = binary_to_decimal(binary_number)
print(f"Decimal of {binary_number}: {decimal_number}")
