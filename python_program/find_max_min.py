# Find Maximum and Minimum: Find the maximum and minimum values in a list of numbers.
def find_min_max(arr):
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

data = [20,12,14,15,123, 10, 115]
maximum, minimum = find_min_max(data)
print(f"List : {data}\n\tMaximum: {maximum}\n\tMinimum: {minimum}")