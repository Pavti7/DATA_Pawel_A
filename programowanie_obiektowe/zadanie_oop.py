# Napisz klasę Student, która posiada pozycje/argumenty:
# class Student:# moje nieudolne próby...
#     def __init__(self, imie: str, nazwisko: str, ocena: list, srednia: float):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.ocena = (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
#         self.srednia = srednia
#         self.spec = []
#
# ocena = 0
# srednia = 0.0
# n = int(init(ocena))
# def add_grade(self):# moje nieudolne próby...
#     if self.ocena:
#         self.ocena = n# moje nieudolne próby...
#
#
#
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
        self.avg_grade = 0.0

    def add_grade(self, grade):
        if grade in (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0):
            self.grades.append(grade)
            self.avg_grade = sum(self.grades) / len(self.grades)
            print("Dodano oceną ")
        else:
            print("Ocena nieprawidłowa ")

s1 = Student("Jan", "Kowalski")
print(s1.first_name, s1.grades, s1.avg_grade)
s1.add_grade(5.0)
s1.add_grade(2.3)
s1.add_grade(4.0)
print(s1.first_name, s1.grades, s1.avg_grade)