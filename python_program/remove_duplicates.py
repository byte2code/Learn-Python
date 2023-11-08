# Remove Duplicates: Remove duplicates from a list
def remove_duplicates(arr):
    unique_list = []
    # unique_list = list(set(arr))
    # [unique_list.append(x) for x in arr if x not in unique_list]
    for x in arr:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

data = [1,2,2,4,5,6,3,3,4,5,6]
result = remove_duplicates(data)
print(f"{remove_duplicates([1,2,2,4,5,6,3,3,4,5,6]) = }")