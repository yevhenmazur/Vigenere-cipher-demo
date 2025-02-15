import sys
import argparse
from _common import register_common_cli_params, normalize_text, \
    read_text_from_file, write_text_to_file
from caesars_cipher import caesar_encrypt, caesar_decrypt
from analyze import frequency_analysis, split_text, recover_vigenere_key
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from kasiski_method import kasiski_analysis


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
                print(
                    f'The text is encrypted with Caesar\'s cipher and written to the file {args.output}')
            else:
                print('The text is encrypted with Caesar\'s cipher:\n')
                print(ciphertext)

        elif args.action == 'decrypt':
            ciphertext = input_text
            plaintext = caesar_decrypt(ciphertext, key)
            if args.output:
                write_text_to_file(plaintext, args.output)
                print(
                    f'The text is decrypted and written to the file {args.output}')
            else:
                print('The text is decrypted with Caesar\'s cipher:\n')
                print(plaintext)

        elif args.action == 'analyze':
            with open(args.input, 'r', encoding="utf-8") as file:
                cipher_text = file.read()
            key = frequency_analysis(cipher_text)
            print(f'The likely encryption key for the Caesar cipher - {key}')

    elif args.method == 'vigenere':

        if args.action == 'encrypt':
            ciphertext = vigenere_encrypt(input_text, args.key)
            if args.output:
                write_text_to_file(ciphertext, args.output)
                print(
                    f'The text is encrypted and written to the file {args.output}')
            else:
                print('The text is encrypted with Vigenere cipher:\n')
                print(ciphertext)

        elif args.action == 'decrypt':
            decrypted_text = vigenere_decrypt(input_text, args.key)

            if args.output:
                write_text_to_file(decrypted_text, args.output)
                print(
                    f'The text is decrypted and written to the file {args.output}')
            else:
                print('The text is decrypted with Vigenere cipher:\n')
                print(decrypted_text)

    elif args.method == 'kasiski':
        key_shifts = []
        filtered_divisor, result = kasiski_analysis(
            input_text, sequence_length=3)
        print(f'The probable length of the Vigenere key - {filtered_divisor}')
        groups = split_text(input_text, filtered_divisor)
        for group in groups:
            group_key = frequency_analysis(group)
            key_shifts.append(group_key)

        vigenere_key = recover_vigenere_key(key_shifts)
        print(f'Recovered Vigenere key is - {vigenere_key}')

    elif args.input:
        with open(args.input, 'r', encoding="utf-8") as file:
            input_file_content = file.read()
    else:
        print('Use --print or --data options')
        exit(1)
