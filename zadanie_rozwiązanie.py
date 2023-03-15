# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usun
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usun - wykonujemy pop()
# Funkcja niczego nie zwraca
lista= [1, 2, 3, 4, 5]
def manage_list(option, value):
    if option == "dodaj":
        lista.append(value)
    elif option == "usun":
        lista.pop()
print(lista)
manage_list("dodaj", 6)
print(lista)
manage_list("usun", 1)
print(lista)
