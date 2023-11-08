# Calculate the Sum: Calculate and print the sum of two numbers.

# Special Symbols Used for passing arguments in Python:
    # *args (Non-Keyword Arguments)
    # **kwargs (Keyword Arguments)

def calculate_sum(*args):
    """Return sum of numbers\n
        Args: 
            *args(int/float): Any number of argument

        Return: 
            result (int/float): Sum of all numbers
    """
    return f"{args} = {sum(x for x in args)}"

result = calculate_sum(1,2,3,5,4,6.0)
print(result)
