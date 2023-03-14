animals = ["kot", "pies", "słoń", "nietoperz"]
print(len(animals))
print(animals)
animals.append("bóbr")
print(animals)
animals.insert(0, "kaczka")
print(animals)
print(len(animals))
animals.remove("kaczka")
print(animals)

animals.pop(3)
print(animals)
deleted_value = animals.pop(0)
print(animals, deleted_value)

animals[0] = "Mrówka"
print(animals)