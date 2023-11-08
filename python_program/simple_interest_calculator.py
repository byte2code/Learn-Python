# Simple Interest Calculator
def simple_interest_calculator():
    # s = p * r * t / 100
    try:
        principal = int(input("Principal amount: "))
        time = int(input("Time duration (months): "))
        rate = float(input("Rate: "))

        si = (principal * rate * time) / (100 * 12)
        print(f"Simple interest on {principal} at {rate}% for {time} months = {si:.2f}")
    except ValueError:
        print("Invalid Input")
        return

simple_interest_calculator()

