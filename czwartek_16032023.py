# Napisz funkcję, która przyjmuja łańcuch znakowy
#     (dla ułtawienia: same małe litery)
# Przykładowo: alamakotaakotmapierdolca
# Funkcja ma zwrócić słownik (return), który zawiera informacje w postaci:
#     Klucz - litera
#     Wartość - ilość wystąpień litery w tekście
# Przykładowo: dla klucza "l" wartości to 2

txt = "alamakotaakotmapierdolca"
def char_counter(text: str)  -> dict:
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = text.count(c)
    return result

def char_counter_alternative(text: str) -> dict:
    result = {}
    for c in text:
        if c in result.keys():
            result[c] += 1
        else:
            result[c] = 1
    return result

# print(char_counter(txt))
# print(char_counter_alternative(txt))

## -         Pętle robi wszystko co jest w cieciu (tab) drukuje print potem dodaje +1 do n
#            i sprawdzam warunek while jesli jest poprawny to znowu robi to samo jesli nie jest poprawny warunek
#            to przechodzi do linijki ktora nie jest wcieta (Tab)
n = 0#                              #  na liczbach
while n < 10:# jest mniejsze od 10
    print(n ** 2)#potęgowanie
    n += 1# zwiększenie o 1

txt = "Ala ma kota"
n = 0#                               # na literach
while n < len(txt):
    print(txt[n])
    n += 1


for i in range(11):
    print("I:", i, "Potęga:", 2 ** i)
    if i == 5:
        continue
    print("--- --- --- --- ---")

    n = 10
    while n > 0:
        if n == 4:
            break
            print("n =")



# ZADANIA:
# 1.
# Napisz program, gdzie użytkownik podaje liczbę n (int)
# Następnie program wyświetla wszystkie liczby parzyste od 0 do n (włącznie)
# 2.
# Wykorzystując pętle while, program wyświetli wszystkie pierwiastki
#     liczb od 10 do 2 (włącznie) (n ** 0.5)
# 3.
# Napisz program, który sumuje wszystkie liczby całkowite z danego przedziału
# Początek i koniec podaje użytkownik
# Np. start = 10, end = 12, wynik - 33

# ad.1.

# liczba = int(input("Podaj liczbę: "))# kod Kacpra
# for c in range (liczba):# kod Kacpra
#     if c % 2 == 0:# kod Kacpra
#         print("liczba: ", c)# kod Kacpra
#
# # ad.2.
# n = 2# kod Kacpra
# while n <= 10:# kod Kacpra
#     print(n ** 0.5)# kod Kacpra
#     n += 1# kod Kacpra

#1
n = int(input("Podaj liczbę: "))# rozwiązanie Piotra
i = 0# rozwiązanie Piotra
while i <= n:# rozwiązanie Piotra
    print(i)# rozwiązanie Piotra
    i += 2# rozwiązanie Piotra

#2
n = 10
while n >= 2:
    print("Pierwiastek liczby", n, " to:", n ** 0.5)
    n -= 1

#3
s = int(input("Podaj start:"))
e = int(input("Podaj koniec:"))
result = 0

for i in range(s, e + 1):
    result += i

print("Wynik", result)
print("Wynik", sum(range(s, e + 1)))

#                                                         Lista składana
numbers = []
for i in range(11):
    numbers.append(2 ** i)
print(numbers)
# ==
numbers_v2 = [2 ** i for i in range(11)]
print(numbers_v2)

# ciekawostka słownik składany
power_for_2 = {i: 2 ** i for i in range(11)}
print(power_for_2)

#     CIEKAWOSTKA
i = 10
print("Liczba i równa się:", i)
# f"" można wykorzystywaćnie tylko w princie, ale również w tworzeniu zmiennych
print(f"Moje i równa się {i}, a potęga 2'1 to: {2 ** i}")
animal_count = 10
info = f"Ala posiada {animal_count} kotów"
worse_info = "Ala posiada " + str(animal_count) + " kotów"
print(info)
