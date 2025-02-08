import sys
import argparse
from _common import register_common_cli_params, normalize_text, read_text_from_file, write_text_to_file
from caesars_cipher import caesar_encrypt, caesar_decrypt
from analyze import frequency_analysis
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    register_common_cli_params(parser)
    args = parser.parse_args()


    input_text = read_text_from_file(args.input)
    input_text = normalize_text(input_text)
    
    if args.method == 'caesars':
        try:
            key = int(args.key)
        except ValueError:
            print('--key argument must be an integer.')
            sys.exit()
        
        if args.action == 'encrypt':
            ciphertext = caesar_encrypt(input_text, key)
            if args.output:
                write_text_to_file(ciphertext, args.output)
            else:
                print(ciphertext)
       
        elif args.action == 'decrypt':
            ciphertext = input_text
            plaintext = caesar_decrypt(ciphertext, key)
            if args.output:
                write_text_to_file(plaintext, args.output)
            else:
                print(plaintext)

    elif args.method == 'vigenere':
        if args.action == 'encrypt':
            ciphertext = vigenere_encrypt(input_text, args.key)
            if args.output:
                write_text_to_file(ciphertext, args.output)
            else:
                print(ciphertext)

        elif args.action == 'decrypt':
            decrypted_text = vigenere_decrypt(input_text, args.key)
            
            if args.output:
                write_text_to_file(decrypted_text, args.output)
            else:
                print(decrypted_text)

    elif args.action == 'analyze':
        with open(args.input, 'r', encoding="utf-8") as file:
            cipher_text = file.read()
        key = frequency_analysis(cipher_text)
        print(f'The likely encryption key for the Caesar cipher - {key}')
    elif args.input:
        with open(args.input, 'r', encoding="utf-8") as file:
            input_file_content = file.read()
    else:
        print('Use --print or --data options')
        exit(1)