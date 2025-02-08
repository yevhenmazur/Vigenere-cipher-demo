'''The module performs encryption and decryption using the Vigenere algorithm.'''

def extend_key(text, key):
    '''If the key is shorter than plaintext, then expand it to the size of plaintext'''
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)


def vigenere_encrypt(text, key):
    '''Encrypt text using the Vigenere cipher'''
    text = text.upper()
    key = extend_key(text, key.upper())
    cipher_text = []
    for i, char in enumerate(text):
        if char.isalpha():  # Лише літери обробляються
            x = (ord(char) + ord(key[i]) - 2 * ord('A')) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        else:
            cipher_text.append(char)  # Інші символи додаються без змін
    return ''.join(cipher_text)


def vigenere_decrypt(cipher_text, key):
    '''Decrypt the text using the Vigenere cipher'''
    cipher_text = cipher_text.upper()
    key = extend_key(cipher_text, key.upper())
    original_text = []
    for i, char in enumerate(cipher_text):
        if char.isalpha():  # Лише літери обробляються
            x = (ord(char) - ord(key[i]) + 26) % 26
            x += ord('A')
            original_text.append(chr(x))
        else:
            original_text.append(char)  # Інші символи додаються без змін
    return ''.join(original_text)
