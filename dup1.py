accounts = [
    ("A001", "100600", 250.50),
    ("B001", "200800", 1999.97),
    ("A002", "600100", 62780.00)
]
# Dla przykładu powyżej:
#             0       1       2
#     0   [0][0]  [0][1]  [0][2]
#     1   [1][0]  [1][1]  [1][2]
#     2
print(accounts)
print(accounts[-1])
print(accounts[-1][2])
print(accounts[0][2], accounts[1][2])

# Pętla ***** for *******
# 1. Łańcuch znakowy
for c in "KOTEK":# c - dla liczb, i - dla cyfr
    print("Litera:", c)

# 2. Łańcuch znakowy -> lista
for word in "Ala ma kota" .split(" "):
    print("Słowo:", word)

#3. lista/krotka
for element in accounts:
    print("Klient:", element)

# 4. Sekwencja liczb (range) -> range - (start, end, step) | <start, end-1>
# Domyślnie krok = 1
# range (10) - <0,9>
# range(1,12) - <1,11>
# range (2,10,2) - <2,9> z krokiem 2

# 4a. Ciąg malejący
for i in range(2, 10, 3):# (od 2, do 10, co 3)
    print("Liczba:", i)
for i in range(10, -1, -1):
    print(i)


