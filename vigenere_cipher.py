'''The module performs encryption and decryption using the Vigenere algorithm.'''
import string

# def extend_key(text, key):
#     '''If the key is shorter than plaintext, then expand it to the size of plaintext'''
#     key = list(key)
#     if len(text) == len(key):
#         return key
#     else:
#         for i in range(len(text) - len(key)):
#             key.append(key[i % len(key)])
#     return ''.join(key)

def extend_key(text, key):
    '''If the key is shorter than plaintext, then expand it to the size of plaintext'''
    key = key.lower()
    extended_key = []
    key_index = 0
    key_length = len(key)

    for char in text:
        if char in string.ascii_letters:  # Додаємо тільки для літер
            extended_key.append(key[key_index % key_length])
            key_index += 1
        else:
            extended_key.append(char)  # Інші символи залишаємо без змін

    return ''.join(extended_key)


def vigenere_encrypt(text, key):
    '''Encrypt text using the Vigenere cipher'''
    text = text.lower()
    key = extend_key(text, key.lower())
    cipher_text = []
    for i, char in enumerate(text):
        if char.isalpha():  # Лише літери обробляються
            x = (ord(char) + ord(key[i]) - 2 * ord('a')) % 26
            x += ord('a')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(char)  # Інші символи додаються без змін
    return ''.join(cipher_text)


def vigenere_decrypt(cipher_text, key):
    '''Decrypt the text using the Vigenere cipher'''
    cipher_text = cipher_text.lower()
    key = extend_key(cipher_text, key.lower())
    original_text = []
    for i, char in enumerate(cipher_text):
        if char.isalpha():  # Лише літери обробляються
            x = (ord(char) - ord(key[i]) + 26) % 26
            x += ord('a')
            original_text.append(chr(x))
        else:
            original_text.append(char)  # Інші символи додаються без змін
    return ''.join(original_text)

if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")
