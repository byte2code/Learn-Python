# Insertion Sort: Implement the insertion sort algorithm to sort a list of 
# numbers. 
def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

unsorted_data = [1,5,4,8,3,90,148,121,84,321,0] 
print(f"Original array: {unsorted_data}")
print(f"Sorted: {insertion_sort(unsorted_data)}")