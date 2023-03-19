# Napisać dekorator, dla funkcji która nie przyjmuje żadnych argumentów
# oraz niczego nie zwraca, którego zadaniem jest wyświetlenie po wywołaniu
# funkcji napisu "--- KONIEC ---"

# Sprawdzić w praktyce dla dowolnej utworzonej przez Was funkcji.
def line_decorator(func):
    def wrapper():
        print(f"*********************************************")
        func()
        print(f"                KONIEC")
    return  wrapper

@line_decorator
def weekend():
    print(f"Funkcja")


weekend()