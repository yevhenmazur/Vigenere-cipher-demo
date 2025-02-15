'''Implementation of the Kasiski test for determining the key length in the Vigenere cipher'''
from collections import defaultdict
import re

def find_repeated_sequences(ciphertext, sequence_length=3):
    '''Find repeating sequences in the ciphertext.'''
    ciphertext = re.sub(r'[^a-zA-Z]', '', ciphertext)
    sequences = defaultdict(list)
    for i in range(len(ciphertext) - sequence_length + 1):
        sequence = ciphertext[i:i + sequence_length]
        sequences[sequence].append(i)
    return {seq: pos for seq, pos in sequences.items() if len(pos) > 1}


def calculate_distances(positions):
    '''Calculate distances between positions.'''
    return [positions[i] - positions[i - 1] for i in range(1, len(positions))]


def find_common_divisors(distances):
    '''Find the divisors of distances.'''
    def get_all_divisors(n):
        divisors = set()
        for i in range(2, n//2 + 1):
            if n % i == 0:
                divisors.add(i)
        if n > 1:
            divisors.add(n)
        return divisors

    all_divisors = defaultdict(int)
    for distance in distances:
        for divisor in get_all_divisors(distance):
            all_divisors[divisor] += 1

    res = sorted(all_divisors.items(), key=lambda x: x[1], reverse=True)
    return res


def filter_divisors(divisors):
    '''Filter the divisors to find the most likely key length.'''
    # Сортуємо за спаданням частоти
    divisors = sorted(divisors, key=lambda x: x[1], reverse=True)

    # Беремо перших 10 дільників
    top_divisors = [d[0] for d in divisors[:10]]

    # Проходимося по факторам, починаючи з найбільшого
    for factor in sorted(top_divisors, reverse=True):
        # Витягуємо всі фактори, які мають більшу або рівну частоту
        relevant_divisors = [d for d in divisors if d[1]
                             >= divisors[top_divisors.index(factor)][1]]

        # Перевіряємо, чи ділиться поточний фактор на ці фактори
        if all(factor % d[0] == 0 for d in relevant_divisors):
            # Обчислюємо середню частоту цих факторів
            avg_frequency = sum(
                d[1] for d in relevant_divisors) / len(relevant_divisors)

            # Якщо частота фактора значно нижча за середнє, відкидаємо його
            factor_frequency = divisors[top_divisors.index(factor)][1]
            if factor_frequency < 0.75 * avg_frequency:  # Поріг 75%, можна налаштувати
                continue

            return factor


def kasiski_analysis(ciphertext, sequence_length=3):
    '''Implementation of the Kasiski analysis.'''
    repeated_sequences = find_repeated_sequences(ciphertext, sequence_length)
    distances = []
    for positions in repeated_sequences.values():
        distances.extend(calculate_distances(positions))

    if not distances:
        return "Не знайдено повторюваних послідовностей."

    common_divisors = find_common_divisors(distances)

    return filter_divisors(common_divisors), common_divisors


if __name__ == "__main__":
    print(f"Direct execution of {__file__} is not allowed. Please run main.py")