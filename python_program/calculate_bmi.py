# Calculate BMI (Body Mass Index): Calculate and categorize BMI based on weight and height inputs.

def calculate_bmi(weight_kg: float, height_m: float) -> str:
    # BMI = weight (kg) / (height (m) * height (m))
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = 70
height = 1.70
bmi = calculate_bmi(weight, height)
print(f'Weight : {weight} kg, Height: {height*100} cms')
print("BMI", ":", bmi)