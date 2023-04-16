
#lista danych:
data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300),
    ("menel", 550),
]

# Należy przepisać powyższe krotki do słownika danych według poniższego schematu:
#     klucz - 1 wartość krotki
#     wartość - 2 wartość krotki podzielona przez 50
#
#     Przykładowo dla pierwsze elementu listy powinnyśmy otrzymać wpis:
#     "Adam": 15
#
#     Program ma pomijać klucze które są duplikowane (wchodzi pierwsze wystąpienie),
#     czyli drugi "Adam" powinien być pominięty w przetwarzaniu.

#Rozwiązanie:

def krotkatodict( zbior :list)->dict:
    slownik = dict()
    for element in zbior:
        if not element[0] in slownik: #pojedyńczy element zawiera np. ("Adam", 750 ), gdzie adam ma index 0 a 750 ma index 1
            slownik[element[0]]=int(element[1]/50) # slownik("Adam")= 750 / 50
    return slownik
a=(krotkatodict(data))
print(a)