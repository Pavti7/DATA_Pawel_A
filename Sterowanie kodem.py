# Warunki arytmetyczne
cost = 2.9
product = "cebula"
if cost >= 3:
    print("Nie kupuj, bo za drogie!!")
else:
    print("Kupuj bo tanio :)")

# Operatory: not, and, or
if product == "cebula" and cost < 3:
    print("Kupuj tą cebulę, chłopie!")
else:
    print("Unikaj jak ogni, bo w chuj drogie!")

# Operator in / not in (później) oraz przedziały
# Przypadek: Oceny są z zakresu 2.0 do 5.0

ocena = 4.5
if 2 <= ocena <= 5:
    print("Ocena prawidłowa")
else:
    print("Ocena nieprawidłowa")

# elif - sprawdza kolejny warunek, jak poprzedni był nieprawidłowy
cost = 3.10
product = "cebula"

if product == "cebula" and cost <= 3:
    print("Kupujesz cebulę")
elif product == "marchewka" and cost <= 4.5:
    print("Kupujesz marchewkę")
elif product == "zgniła cebula" and cost <= 1.9:
    print("Nie kup[uj tego gówna")
else:
    print("Wychodzisz bez zakupów.")