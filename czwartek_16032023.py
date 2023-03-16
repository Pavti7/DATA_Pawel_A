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