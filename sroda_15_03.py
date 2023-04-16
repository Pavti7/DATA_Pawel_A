# Słownik
contacts = {
    "Paweł": "605152088",
    "Asia": "601658216",
    "Sopot": "+48565513013"

}

print(len(contacts))
# Dostęp do kluczy, wartości, elementów
print(contacts.keys())
print(contacts.values())
print(contacts.items())

if "Paweł" in contacts.keys():
    print("Kontakt istnieje.")

# Dodawanie nowych kluczy | Modyfikacja wartości
contacts["Iza"] = "1234567"
print(contacts)
contacts["Paweł"] = "+48605152088"
print(contacts.keys())

# Wyświetlanie wybranej wartości
print(contacts["Paweł"])
#1 (sposób na sprawdzenie)
print(contacts.get("Bożydar", "Kontakt nie istnieje."))
#2 (sposób na sprawdzenie)
if "Bożydar" in contacts.keys():
    print(contacts["Bożydar"])
else:
    print(-1)

# Usuwanie kluczy (oraz ich wartości)
contacts.pop("Sopot") # w tym przypadku pop nie może być arg.
print(contacts)

# Przepisywanie pod nowy klucz
contacts["Adam"] = contacts.pop("Paweł")
print(contacts)
del contacts["Iza"] # Dla ciekawskich
print(contacts)

def add_contacts(con_dict: dict, key: str, value: str):
    if key in con_dict.keys():
        print("Kontakt istnieje")
    else:
        con_dict[key] = value
        print("Kontakt dodano")

contacts2 = {
            "Ewa": "00988765432"

        }
add_contacts(contacts2, "Ewa", "47457453")
add_contacts(contacts2, "Adam", "76553435")
print(contacts2)

# Krotka (tuple)
metadata = ("Python w DS", "1.0", "20230315", "20230315")
print(metadata)
print(metadata[0], metadata[3], len(metadata))
print(metadata.count("20230315"))

# Zbiór
numbers = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3}
#Pusty zbiór: n = set()
print(numbers)
numbers.add(9)# dodanie pojedynczego elementu
numbers.update([1, 4, 5, 2, 0, 11]) # Dodanie listy elementów
numbers.update(["a", "b", "c"])
print(numbers)
