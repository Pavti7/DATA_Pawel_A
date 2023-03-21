# Napisać program któryu zliczy ilość wytąpień każdego słowa z pliku o nazwie reduta.txt

words = {}
with open("reduta.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.replace("\n", "").split(" "):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1

print(words)