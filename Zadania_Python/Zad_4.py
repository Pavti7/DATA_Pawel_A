# Zadanie 04
# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje. Program działa dopóki użytkownik nie poda liczby ujemnej.
# Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.
n = int(input("Podaj liczbę: "))
summary = 0

while n >= 0:
    summary += n
    n = int(input("Podaj liczbę: "))

print(f"Suma podstawionyh liczb to: {summary}")