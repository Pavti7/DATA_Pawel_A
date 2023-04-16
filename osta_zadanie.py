
lista= [1, 2, 3, 4, 5]
print(lista)
print(len(lista), "<- to ilość cyfr z listy")
print(sum(lista), "<- to suma liczb z listy")
x = int(input("podaj liczbę którą chcesz +/-: "))
y = (sum(lista))
if x < 0:
    lista.pop(x)
    print("wynik pomniejszony o podaną liczbę to: ", sum(lista))
    print(lista)
elif x >= 0:
    lista.append(x)
    print("wynik po dodaniu podanej cyfry to:  ", sum(lista))
    print(lista)


# input("jaką liczbę chcesz dodać lub odjąć? ")

# input("Naciśnij enter")
# animals = ["kot", "pies", "ptak", "nosorożec"]
# print(index(animals, 5))
# print(len(animals))
# print(animals[0], animals[1], animals[-1])
# print(animals[0])
# print(animals[1])
# print(animals[2])
# print(animals[-1])
#
# print(len(animals))
# animals.append("bóbr")
# print(animals)
# print(len(animals))
# animals.insert(0, "kaczka")
# print(animals)
# print(len(animals))
# animals.remove("kaczka")
# print(animals)
# animals.pop()
# print(animals)
# print(len(animals))
# deleted_value = animals.pop(0)
# print(animals, deleted_value)

# animals[0] = "Mrówka"
# print(animals)