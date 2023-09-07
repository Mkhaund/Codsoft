import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "No characters selected for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example:
password = generate_password(length=16, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True)
print("Generated Password:", password)
