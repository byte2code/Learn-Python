# Linear Search: Implement linear search to find an element in a list. 
def linear_search(arr: list, key: int) -> int:
    for i in arr:
        if i == key:
            return arr.index(i) + 1
    return -1

data = [1,2,3,4,5,6,8]
key = 5

result = linear_search(data, key)
print(f"Array: {data}, No to find: {key}\n\tFound at: {result}")