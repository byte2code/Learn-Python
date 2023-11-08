# Basic Calculator: Build a basic calculator that performs 
# addition, subtraction, multiplication, and division.

class Calculator:
    """
    A basic calculator class that performs addition, 
    subtraction, multiplication, and division.

    Attributes:
        result (float): Current Result.

    Methods:
        add(x, y):      Perform addition of two numbers.
        subtract(x, y): Perform subtraction of two numbers.
        multiply(x, y): Perform multiplication of two numbers.
        divide(x, y):   Perform division of two numbers.
        calculate():    Performing calculation.
    """
    def __init__(self) -> None:
        self.result = 0
        self.operation = None
    
    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result = x / y
    
    def calculate(self):
        while True:
            print("\nSelect Operation to perform:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("0. Exit")

            try:
                menu = int(input("Choose operation: "))
            except ValueError:
                print("Please enter a valid choice.")
                continue

            if menu == 0:
                print("**Thank you**")
                break
            elif menu not in (1, 2, 3, 4):
                print("Please select a valid choice (1-4).")
                continue

            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if menu == 1:
                self.add(x, y)
                self.operation = "Addition"
            elif menu == 2:
                self.subtract(x, y)
                self.operation = "Subtraction"
            elif menu == 3:
                self.multiply(x, y)
                self.operation = "Multiplication"
            elif menu == 4:
                try:
                    self.divide(x, y)
                    self.operation = "Division"
                except ValueError as e:
                    print(e)
                    continue

            print(f"{self.operation} Result: {self.result}")

    def __str__(self):
        return f"[+] Operation performed: {self.operation}\n[+] Obtained Result: {self.result}"

if __name__ == '__main__':
    calculator = Calculator()
    calculator.calculate()
    print(calculator)
