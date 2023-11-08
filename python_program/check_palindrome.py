# Check Palindrome: Determine if a string is a palindrome
def check_palindrome_slicing(s):
    return True if s == s[::-1] else False

def check_palindrome(s):
    len_s = len(s)
    for i in range(len_s):
        if s[i] == s[len_s - i - 1]:
            continue
        else:
            return False
    return True

print(f"{check_palindrome('malaylam') = }")
print(f"{check_palindrome_slicing('malayalam') = }")