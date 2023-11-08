# Generate Random Password: Generate a random password of a specified length.
import string
import secrets
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
def generate_random_password(pass_len):
    characters = string.digits + string.ascii_letters + string.punctuation
    password = ''.join(secrets.choice(characters) for x in range(pass_len))
    return password

password = generate_random_password(12)
print(f"Random password with length 12 = {password}")