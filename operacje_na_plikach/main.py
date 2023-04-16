
with open("names.txt", "r", encoding="utf-8") as file:

    for line in file:
        tmp = line.replace('\n', '')
#        print(f"{tmp} - {len(tmp)}")
        print(file.readlines(2))
#        print(line, end="")
#    print(file.read())
#    print(file.readline())
#    print(f"{line.replace('\n', '')} - {len(line.replace('\n', ''))}")

