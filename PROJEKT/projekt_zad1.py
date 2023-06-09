# Zadanie 01
# Napisz program który pozwoli wygenerować dowolną liczbę (wierszy) danych według poniższego schematu
#
# godzina:minuta
# wartość od 0 do 100
# wartość od 0.1 do 1.0
# Każde wartości powinny być oddzielone średnikami czas;war1;war2
#
# W przypadku losowości wartości użyjecie randint oraz uniform (obie znajdują się w random) Natomiast godzina:minuta ma być również losowana (do funkcji timedelta wykorzystać randint)
#
# nazwa pliku: dane_dzienmiesiacrok
#
# Zadanie 02
# Wykorzystując dane z Zadanie 01:
#
# Dodać nową kolumnę do pliku (można do nowego), która będzie wynikiem operacji matematycznej: kol2 * kol3, natomiast pierwsza kolumna ma posiadać informacje tylko o godzinie.
#
# Ostatecznie:
#
# Godzina
# war1 (0-100)
# war2 (0.1-1.0)
# war1 * war2

with open("dane_20230323.txt", "r", encoding="utf-8") as file:
    with open("dane_20230323_processing.txt", "a", encoding="utf-8") as output:
        for line in file:
            tmp = line.replace("\n", "").split(";")
            row = tmp[0][:2] + ";" \
                  + tmp[1] + ";" + tmp[2] \
                  + ";" + str(round(float(tmp[1]) * float(tmp[2]), 2)) + "\n"
            output.write(row)