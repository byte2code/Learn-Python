# Find the Length of a List: Calculate the length of a list without using the 
# built-in len function. 

def find_list_length(arr):
    length = 0
    for i in arr:
        length += 1
    return length

data = [1,2,3,4,5,6,9]
print(f"{find_list_length() = }")