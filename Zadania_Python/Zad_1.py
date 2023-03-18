# Zadanie 01
# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina. Funkcja przyjmuje jako argument temperaturę w C,
# a funkcja zwraca temperaturę w K. Więcej informacji o konwersji:
# https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html
# Obie wartości maja być typu float

def celsius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


print(celsius_to_kelvin(10))
print(celsius_to_kelvin(-273.15))
print(celsius_to_kelvin(-50.0))
print(celsius_to_kelvin(-17))