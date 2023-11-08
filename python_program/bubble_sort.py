# Bubble Sort: Implement the bubble sort algorithm to sort a list of numbers.
unsorted_data = [1,5,4,8,3,90,148,121,84,321,0] 
def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
    return arr

unsorted_data = [1,5,4,8,3,90,148,121,84,321,0] 
print(f"Original array: {unsorted_data}")
print(f"Sorted: {bubble_sort(unsorted_data)}") 