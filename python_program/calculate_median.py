# Calculate Median: Calculate the median of a list of numbers.

def calculate_median(arr):
    arr_len = len(arr)
    median = 0
    if arr_len % 2:
        median = arr[(arr_len + 1)//2 - 1]
    else:
        median = arr[(arr_len//2) - 1] + arr[(arr_len//2)]
        median /= 2
    return median

even = [1,2,3,4,5,6,8,9]
odd = [1,2,3,4,6,8,9]
print(f"Median of {even} = {calculate_median(even)}")
print(f"Median of {odd} = {calculate_median(odd)}")