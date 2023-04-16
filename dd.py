# Zadanie 1
# Napisz funkcję, która jak argument przyjmuje listę liczby całkowitych,
# a zwraca wartość int jako największa liczba z listy (nie wolno używać max).
# # Dodatkowo zabezpiecz program, przed błednymi danymi (np. tekst)
lista = ["drakula", 1, 23, "karamba", 23, 5, 7]

def maximum(lista: list)-> int:
    result=0
    for number in lista:
        try:
            if number>=result:
                result=number
        except TypeError:
            continue
    return result

print(maximum(lista))

# Zadanie 2
# Napisz moduł, który będzie posiadał funkcje obliczające:
#
# Funkcje kwadratową (zwraca listę rozwiązań)
# Pierwiastek drugiego stopnia z podanej liczby
# N element ciągu harmonicznego (prośba o weryfikacje czym jest ciag z netem)
def funkcje(rodzaj:str, a:int, b=0, c=0 ):
    try:
        if rodzaj == "kwadrat":
            delta = (b ** 2) - (4 * a * c)
            if delta > 0:
                x1 = (-b - delta * (1 / 2)) / (2 * a)
                x2 = (-b + delta * (1 / 2)) / (2 * a)
                return [x1, x2]
            elif delta == 0:
                x0 = -b / (2 * a)
                return x0
            else:
                print('brak rozwiązań')
    except TypeError:
        print("Nie poprawne wartosci Kurwo")
    if rodzaj =="sqrt":
        return a**(1/2)
    if rodzaj == "ciąg":
        return float(1/a)



print(funkcje("kwadrat", 2, 4, 1))
print(funkcje("sqrt",9))
print(funkcje("ciąg", 32))

#Zadanie 3
# Napisz program, który narysuje trójkąt zależnie od podanego n
#
# Np. n = 3 to wynik jest
#
# *
# **
# ***
# Dodaj dekorator, który dodatkowo dopisze "-----------" na dole trójkąta oraz policzy liczbę *
def zliczanie(n):
    suma=0
    for a in range(n+1):
        suma+=a
    return suma

def podloga(n):
    z = ""
    for i in range(n):
        z += "-"
    return z


def dekorator(func):
    def wrapper(a):
        func(a)
        print(podloga(a))
        print(f"Suma gwizadek wynosi: {zliczanie(a)}")
    return wrapper

@dekorator
def triangle(n:int)->None:
    m = ""
    r = 0
    while r < n:
        m = m + "*"
        print(m)
        r += 1

triangle(13)