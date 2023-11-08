# Reverse a String: Reverse a given string
def reverse_string_slicing(s):
    print(s[::-1])

def reverse_string(s):
    r = ""
    for char in s:
        r = char + r
    print(r)

print(f'{reverse_string_slicing("MausamGiri") =}')
print(f"{reverse_string('MausamGiri') =}")