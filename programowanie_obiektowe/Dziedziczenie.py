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
    def __init__(self, name: str, surname: str, adres: str, age: int):
        self.name = name
        self.surname = surname
        self.adres = adres
        self.age = age

    def check_is_adult(self):
        if self.age  := 18
        return True

 class Castomer(Person):
     def __init__(self, name: str, surname: str, adres: str, age: int):
         super().__init__(name, surname, adres, age)
p1 = Person("Jan", "Kowalski", "Gdańsk", 21)
print(p1)