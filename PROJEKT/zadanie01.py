# Zadanie 01
# Napisz program który pozwoli wygenerować dowolną liczbę (wierszy) danych według poniższego schematu
#
# godzina:minuta
# wartość od 0 do 100
# wartość od 0.1 do 1.0
# Każde wartości powinny być oddzielone średnikami czas;war1;war2
#
# W przypadku losowości wartości użyjecie randint oraz uniform (obie znajdują się w random) Natomiast godzina:minuta ma być również losowana (do funkcji timedelta wykorzystać randint)
#
# nazwa pliku: dane_dzienmiesiacrok

from random import randrange
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

n = int(input("Podaj ilość dat: "))

    for l in range(n):
        numbers = set()
        while len(numbers) < 3:
            numbers.add(f"{randint(0, 100)} ")

    with open("dane_dzienmiesiacrok.txt", "a+", encoding="utf-8") as file:
        file.writelines(numbers)
        file.write("\n")