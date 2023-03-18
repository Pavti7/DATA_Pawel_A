class Animals:
    def __init__(self, legs_count, eyes_count, name, weight):
        self.legs_count = legs_count
        self.eyes_count = eyes_count
        self.name = name
        self.is_alive = True
        self.weight = weight

    def __str__(self):
        return self.name
#        return f"{super().__str__()} - {self.race}"# alternatywne rozwiązanie z dziedziczeniem
    def running(self):
        print(f"{self.name} - tup, tup. tup, tup....")
class Dog(Animals):
    def __init__(self, legs_count, eyes_count, name, weight, race):
        super().__init__(legs_count, eyes_count, name, weight)
        self.race = race

d1 = Dog(4, 2, "Burek", 30, "Husky")
print(d1.is_alive, d1.race)
print(d1.is_alive, d1)
print(d1)
d1.running()

