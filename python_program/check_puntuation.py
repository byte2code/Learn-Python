# Check Punctuation: Determine if a character is a punctuation symbol. 

import string

def check_punctuation(character):
    punct = string.punctuation
    return True if character in punct else False

print(f"{check_punctuation(':') = }")
