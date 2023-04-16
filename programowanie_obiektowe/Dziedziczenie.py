# Napisać klasę Person, która zawiera pola:
#     - imie (str)
#     - nazwisko (str)
#     - adres (str)
#     - wiek (int)
# Dodatkowo klasa posiada metody:
#     - __str__ - zwraca tekst w formacie: "Nazwisko, Imie, adres"
#     - check_is_adult() - zwraca true, jeżeli wiek >= 18
#
# Napisać klasę Customer, która dziedziczy po Person, a dodatkowo:
# Posiada pola:
#     - orders (list)
#     - login (str)
#     - total_order_cost (float)
# Oraz funkcje:
#     - str - wykorzystuje dziedziczony str, a dodatkowo na początku podaje login
#     - add_order(product, cost) - dodaje krotke do listy zamowien
#         Można dodać zamówienie tylko jak użytkownik jest pełnoletni
#         Dodatkowo aktualizuje wartość total_order_cost po dodaniu zamówienia
#     - show_orders() - wyświetla wszystkie zamówienia (jeden pod drugim)

class Person:
    def __init__(self, name, surname, adres, age):
        self.name = name
        self.surname = surname
        self.adres = adres
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.adres}"

    def check_is_adult(self):
        return self.age >= 18

class Castomer(Person):
    def __init__(self, name, surname, adres, age):
         super().__init__(name, surname, adres, age)
         self.login = login
         self.orders = []
         self.total_order_cost = 0.0
    def __str__(self):
        return f"{self.login} - {super().__str__()}"
    def add_order(self, produkt, cost):
        if super().check.append((product, cost))
            self.orders.append((produkt, cost))
            self.total_order_cost += cost
        else:
            print("Osoba nie jest pełnoletnia!")

    def show orders(self):
        for e in self.orders:
            print(e)





p1 = Person("Jan", "Kowalski", "Gdańsk", 21)
print(p1)