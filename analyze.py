'''The module contains functions for frequency analysis.'''
from collections import Counter
import string


def frequency_analysis(text: str) -> int:
    '''
    Performs frequency analysis of text.
    Returns the value of the alphabetical order shift.
    '''
    text = ''.join([char for char in text if char in string.ascii_lowercase])
    freq = Counter(text)
    # sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    most_common_char = max(freq, key=freq.get)
    typical_most_common_char = 'e'
    shift = (ord(most_common_char) - ord(typical_most_common_char)) % 26

    return shift


def split_text(cipher_text, key_length):
    '''Splits Vigenere ciphertext into groups suitable for frequency analysis'''
    groups = ['' for _ in range(key_length)]
    index = 0  # Лічильник тільки для літер

    for char in cipher_text:
        if char in string.ascii_lowercase:  # Беремо до уваги тільки літери
            groups[index % key_length] += char
            index += 1  # Рахуємо лише букви

    return groups


def recover_vigenere_key(shifts):
    """Відновлює буквений ключ Віженера із списку зсувів"""
    return ''.join(chr(shift + ord('a')) for shift in shifts)


if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")
