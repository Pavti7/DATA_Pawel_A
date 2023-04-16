try:
    print(10 / 0)
    print("Ala ma " + 5 + "kotów.")
except ZeroDivisionError:
    print("Próbowano dzielić przez zero")
except TypeError:
    print("Wystąpił problem z typem danych")

# Do zadania nr 4 z pracy domowej dopisz zabezpeczenie, jeżeli użytkownik poda
# informację, której nie można konwertować na int

# Rozwiń funkcjonalność zadania z (opcja, *args) o nową opcję "iloraz".
# Zabezpiecz program, że w przypadku dzielenia przez zero kontynuuj działanie
# iloraz (dzielenia kolejnych wartości), pomijając błędny (umieść continue w except)

n = int(input("Podaj liczbę: "))
summary = 0

while n >= 0:
    summary += n
    n = int(input("Podaj liczbę: "))

print(f"Suma podstawionyh liczb to: {summary}")
def calculation(option: str, *args) -> float:
    result = args[0]
    if option == "iloczyn":
        for i in range(1, len(args)):
            result *= args[i]
        return result
    else:
        return args[0]

print(calculation({summary}, 4)
