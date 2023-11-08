# Selection Sort: Implement the selection sort algorithm to sort a list of 
# numbers. 
def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

unsorted_data = [1,5,4,8,3,90,148,121,84,321,0] 
print(f"Original array: {unsorted_data}")
print(f"Sorted: {selection_sort(unsorted_data)}")