# Vigenere-cipher-demo
The scripts contain implementations of the Caesar and Vigenère ciphers, as well as tools for frequency analysis and Kasiski analysis for the Vigenère cipher.

Encrypt with Caesar's cipher

```
python main.py -m caesars -a encrypt -i plaintext.txt -o ciphertext.txt -k 3
```

Decrypt the Caesar's cipher

```
python main.py -m caesars -a decrypt -i ciphertext.txt -k 3
```

Frequency analysis

```
python main.py -m caesars -a analyze -i ciphertext.txt
```

Encrypt with the Vigenere cipher

```
python main.py -m vigenere -a encrypt -i plaintext.txt -o ciphertext.txt -k secret
```

Decrypt the Vigenere cipher

```
python main.py -m vigenere -a decrypt -i ciphertext.txt -k secret
```

Analyze the Vigenère ciphertext using the Kosiski method and frequency analysis


```
python main.py -m kasiski -a analyze -i ciphertext.txt
```