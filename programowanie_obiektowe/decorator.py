# Dekorator dla funkcji, która nie przyjmuje argumentów i nic nie zwraca
def line_decorator(func):
    def wrapper():
        print(f"--------------------------------------------------")
        func()
        print(f"--------------------------------------------------")
    return  wrapper

@line_decorator
def my_date() -> None:
    print(f"Dzisiaj jest 19-03-2023")
@line_decorator
def my_curse() -> None:
    print(f"ARPDataPL9")

my_date()
my_curse()

# Dekorator dla funkcji, która przyjmuje argumenty oraz niczego nie zwraca
def trigger_info_none(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        func(*args, **kwargs)
    return wrapper


# Dekorator dla funkcji, która przyjmuje argumenty oraz coś zwraca
def trigger_info_return(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        return func(*args, **kwargs)
    return wrapper