with open("surmanes.txt", "a+", encoding="utf-8") as file:# a+ przy tworzeniu pliku i nadpisywania jego wartości, potem warto zmienić np. na "w"
    file.write("Kowalski\n")
    file.write("Nowak\n")
    file.write("Brzechwa\n")
    file.writelines(("Malinowski\n", "Killer\n", "Pytalski"))

from random import  randint
print(randint(1, 49))

