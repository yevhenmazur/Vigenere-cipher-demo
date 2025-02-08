from collections import Counter
import string

def frequency_analysis(text):
    text = ''.join([char for char in text if char in string.ascii_lowercase])
    freq = Counter(text)
    # sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    most_common_char = max(freq, key=freq.get)
    typical_most_common_char = 'e'
    shift = (ord(most_common_char) - ord(typical_most_common_char)) % 26
    
    return shift

if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")