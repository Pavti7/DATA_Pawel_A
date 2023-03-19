# Napisz funkcję, która jako PIERWSZY argument przyjmuje rodzaj operacji
#     "suma", "różnica", "iloczyn"
# a następnie wykona sumowanie/odejmowanie/mnożenie wszystkich argumentów
# podanych po pierwszym. Ilość argumentów do obliczeń może być dowolna
# Rozwiń funkcjonalność zadania z (opcja, *args) o nową opcję "iloraz".
# Zabezpiecz program, że w przypadku dzielenia przez zero kontynuuj działanie
# iloraz (dzielenia kolejnych wartości), pomijając błędny (umieść continue w except)

def calculation(option: str, *args) -> float:
    result = args[0]
    if len(args) >= 2:
        if option == "suma":
            for i in range(1, len(args)):
                result += args[i]
        elif option == "różnica":
            for i in range(1, len(args)):
                result -= args[i]
        elif option == "iloczyn":
            for i in range(1, len(args)):
                result *= args[i]
        elif option == "iloraz":
            for i in range(1, len(args)):
                try:
                    result /= args[i]
                except ZeroDivisionError:
                    continue
                    
        return result
    else:
        return args[0]

print(calculation("suma", 1, 2, 3))
print(calculation("rożnica", 23, 45, 5))
print(calculation("iloczyn", 2, 2))
print(calculation("różnica", -2))

# ponizej moje nieudolne próby poraczenia sobiew z zadaniem :(
# def summary(*args) -> int:
#     print(f"Elements: {args}")
#     result = 0
#     for i in args:
#         result += i
#
#     return result
# def minus(*args) -> int:
#     print(f"Wynik: {args}")
#     result = 0
#     for i in args:
#         result -= i
# def iloczyn(*args) -> int:
#     print(f"Wynik: {args}")
#     print(f"Wynik: {args}")
#     result = 0
#     for i in args:
#         result *= i
#
# def operacje(prefix: str, *args) -> None:
#     for i in args:
#         print(f"{prefix} -> {i}")
