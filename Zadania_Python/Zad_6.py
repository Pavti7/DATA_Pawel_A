# Zadanie 06
# Użytkownik podaje liczbe całkowitą. Następnie program zwraca sumę CYFR z których składa się podana liczba.
# Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7). Podpowiedź: konwersja na str

number = input("Podaj liczbę: ")
result = 0

for i in number:
    result += int(i)

print(result)
