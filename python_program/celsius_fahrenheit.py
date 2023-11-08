# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        print("Invalid input")

celsius_to_fahrenheit()