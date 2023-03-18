# Zadanie 07
# Napisać program, gdzie użytkownik podaje n łańcuchów znakowych (ilość n również definiuje wcześniej użytkownik).
# Następnie program zwraca informacje ile łańcuchów znakowych jest unikatowych. :)
# Przykładowo: użytkownik podał n = 3. Następnie podał trzy łańcuchy znakowe:
# Kot, Pies, Kot. Program zwróci informacje, że ilość UNIKATOWYCH łańuchów znakowych

n = int(input("Ile danych cghcesz podać?: "))
my_collection = set()

for i in range(n):
    txt = input(f"Podaj txt: {i+1}: ")
    my_collection.add(txt)

print(f"Ilość unikatowych wartości: {len(my_collection)}")
