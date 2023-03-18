# Zadanie 05
# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny (nie używamy funkcji wbudowanych w Pythonie)

def dec_to_bin(value: int) -> list:
    parts = []

    while value != 0:
        parts.append(value % 2)
        value //= 2

    return parts[::-1]
