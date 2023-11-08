# Count Characters in a String: Count the occurrences of each character in a string. 

def count_charaters(s):
    count=0
    for i in s:
        count += 1
    return count

print(f"{count_charaters('mausam giri') = }")