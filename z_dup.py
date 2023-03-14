animals = ["kot", "pies", "słoń", "nietoperz"]
print(animals)
animals.append("bóbr")
print(animals)
animals.insert(0, "kaczka")
print(animals)
animals.remove("kaczka")
print(animals)

deleted_args.append(animals.pop(3))
print(animals)
deleted_value = animals.pop(0)
deleted_args.append(deleted_value)
print(animals, deleted_value)

animals[0] = "Mrówka"
print(animals)
