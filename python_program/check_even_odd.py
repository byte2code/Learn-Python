# Check Even or Odd: Determine if a number is even or odd.

def check_even_odd(num) -> bool:
    """Check does the number is even or odd\n
    Args: 
        num (int) : A number
    
    Return: 
        result (boolean): True/False
    """
    return False if num % 2 else True

result = check_even_odd(10)
print(result)