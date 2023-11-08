# Check Anagrams: Determine if two strings are anagrams of each other. 
def check_anagrams(valA, valB):
    if len(valA) != len(valB):
        return False
    
    checker = {}
    for char in valA:
        checker[char] = checker.get(char, 0) + 1

    for char in valB:
        if not checker.get(char):
            return False
        checker[char] -= 1

    return all(value == 0 for value in checker.values())

print(f"{check_anagrams('mausam', 'mausam') = }")