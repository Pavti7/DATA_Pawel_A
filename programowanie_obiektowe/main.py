class Car:
    def __init__(self, color, price, brand):# __xx__ to tak zwane "magic function" które automatyzują funkcję w odp. momencie i kolejności
        self.color = color# definiujemy parametry zmiennych należących do określonej klasy
        self.price = price
        self.brand = brand
        self.running = False
        self.spec = []

    def __str__(self):
        return f"{self.brand}, {self.color}, {self.price}"

    def __float__(self):
        return  self.price
    def switch(self):
        if self.running:
            self.running = False
        else:
            self.running = True


c1 = Car("Czerwony", 4500000, "Ferrari")
c2 = Car("Zielony", 15000, "Opel")
print(c1.color, c2.color)
print(c1.running, c2.running)
c1.switch()
print(c1.running, c2.running)
print(c1)
txt = str(c1)
c1.color = "Srebrny"
print(c1)