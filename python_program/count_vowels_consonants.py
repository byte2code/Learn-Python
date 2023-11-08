# Count Vowels and Consonants: Count the number of vowels and consonants in a string.

# ord() function is a built-in function that accepts a string containing a single Unicode character and returns an integer representing the Unicode point of that character

def count_vowels_consonants(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = {
        "vowels": 0,
        "consonants": 0
    }
    for char in s:
        if char in vowels:
            count["vowels"] += 1
        
        if char not in vowels and ((ord(char) >= ord("a") and ord(char) <= ord("z")) or \
            (ord(char) >= ord("A") and ord(char) <= ord("Z"))):
            count["consonants"] += 1
    
    return count

print(f"{count_vowels_consonants('Mausam GIRI')}")
