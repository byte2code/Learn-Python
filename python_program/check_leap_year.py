# Check Leap Year 
def check_leap_year(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
year = int(input("Enter a year: "))
result = check_leap_year(year)
print(f"{year} is leap year -> {result}")