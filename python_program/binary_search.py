# Binary Search: Implement binary search to find an element in a sorted list.
def binary_search(arr: list, key: int) -> int:
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1    

data = [1,2,3,4,5,6,8]
key = 5

result = binary_search(data, key)
print(f"Array: {data}, No to find: {key}\n\tFound at: {result}")