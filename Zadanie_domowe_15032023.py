# Mamy listę danych:
# data = [
#     ("Adam", 750),
#     ("Ewa", 250),
#     ("Jakub", 200),
#     ("Elżbieta", 1000),
#     ("Adam", 400),
#     ("Ewa", 300)
# ]
#
# Należy przepisać powyższe krotki do słownika danych według poniższego schematu:
#     klucz - 1 wartość krotki
#     wartość - 2 wartość krotki podzielona przez 50
#
#     Przykładowo dla pierwsze elementu listy powinnyśmy otrzymać wpis:
#     "Adam": 15
#
#     Program ma pomijać klucze które są duplikowane (wchodzi pierwsze wystąpienie),
#     czyli drugi "Adam" powinien być pominięty w przetwarzaniu.

data = [
    ("Adam", 750),
    ("Ewa", 250),
    ("Jakub", 200),
    ("Elżbieta", 1000),
    ("Adam", 400),
    ("Ewa", 300)
]

data_in_dict = {}
for i in range(len(data)):
    if data[i][0] not in data_in_dict.keys():# sprawdzenie czy nie ma duplikatów na liście
        data_in_dict[ data[i][0]] = int(data[i][1] / 50)# alternatywne rozwiązanie tak żeby była liczba całkowita bez ,
        # data_in_dict[ data[i][0]] = data[i][1] / 50
print(data_in_dict)
