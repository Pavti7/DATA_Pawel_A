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

