import sys
import argparse
from _common import register_common_cli_params, normalize_text, read_text_from_file, write_text_to_file
from caesars_cipher import caesar_cipher, caesar_decipher
from analyze import frequency_analysis


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    register_common_cli_params(parser)
    args = parser.parse_args()


    if args.method == 'caesers':
        plaintext = read_text_from_file(args.input)
        plaintext = normalize_text(plaintext)
        try:
            key = int(args.key)
        except ValueError:
            print('--key argument must be an integer.')
            sys.exit()
        
        if args.action == 'encrypt':
            ciphertext = caesar_cipher(plaintext, key)
            if args.output:
                write_text_to_file(ciphertext, args.output)
            else:
                print(ciphertext)
       
        elif args.action == 'decrypt':
            ciphertext = plaintext
            plaintext = caesar_decipher(ciphertext, key)
            if args.output:
                write_text_to_file(plaintext, args.output)
            else:
                print(plaintext)

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