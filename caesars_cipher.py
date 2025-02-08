import string


def caesar_encrypt(text: str, shift: int) -> str:
    '''Encrypts text with the Caesar cipher.'''
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift % 26:] + alphabet[:shift % 26]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def caesar_decrypt(text: str, shift: int) -> str:
    '''Decrypts text encrypted with the Caesar cipher'''
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")
