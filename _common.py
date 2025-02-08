import string

def read_text_from_file(text_file: str) -> str:
    '''Read the text from file'''
    with open(text_file, "r", encoding="utf-8") as file:
        content = file.read()
    return(content)

def write_text_to_file(text: str, text_file: str) -> bool:
    '''Write the text to file'''
    try:
        with open(text_file, "w", encoding="utf-8") as file:
            content = file.write(text)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def normalize_text(text: str) -> str:
    '''Strips out punctuation, converts to lower case, and preserves spaces.'''
    allowed_chars = string.ascii_lowercase + ' '
    text = text.lower()
    return ''.join(char for char in text if char in allowed_chars or char.isspace())

def register_common_cli_params(parser):
    parser.add_argument('--input', '-i', type=str,
                        default="plaintext.txt",
                        help='Path to file with input tetx')

    parser.add_argument('--output', '-o', type=str,
                        # default="ciphertext.txt",
                        help='Path to file with output tetx')

    parser.add_argument('--action', '-a', required=True,
                        choices=["encrypt", "decrypt", "analyze"],
                        help='Action can be encrypt, decrypt, analyze')
    
    parser.add_argument('--key', '-k', default=3,
                        help='The key for encryption or decryption')
    
    parser.add_argument('--method', '-m',
                        choices=["caesars", "vigenere", "kasiski"],
                        help='Path to file with output tetx')

    # parser.add_argument('--output', type=str,
    #                     default="ciphertext.txt",
    #                     help='Path to file with output tetx')

    # parser.add_argument('--output', type=str,
    #                     default="ciphertext.txt",
    #                     help='Path to file with output tetx')


if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")
