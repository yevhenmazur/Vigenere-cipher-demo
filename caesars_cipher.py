import string

def normalize_text(text: str) -> str:
    '''Strips out punctuation, converts to lower case, and preserves spaces.'''
    allowed_chars = string.ascii_lowercase + ' '
    text = text.lower()
    return ''.join(char for char in text if char in allowed_chars or char.isspace())

def caesar_cipher(text: str, shift: int) -> str:
    '''Encrypts text with the Caesar cipher.'''
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift % 26:] + alphabet[:shift % 26]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def caesar_decipher(text: str, shift: int) -> str:
    '''Decrypts text encrypted with the Caesar cipher'''
    return caesar_cipher(text, -shift)

# if __name__ == "__main__":
#     raw_text = "Hello, World! This is a test."
#     normalized = normalize_text(raw_text)
#     encrypted = caesar_cipher(normalized, 3)
#     decrypted = caesar_decipher(encrypted, 3)
    
#     print(f"Normalized: {normalized}")
#     print(f"Encrypted: {encrypted}")
#     print(f"Decrypted: {decrypted}")


if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")
