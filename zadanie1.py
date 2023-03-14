text = "HELLO"

# print(txt[::-2])


text = "HELLO"
def reverse_idx(text, index):
    if 0 <= index <= (len(text) -1):
        return index - len(text)
    else:
        return -999

    print(reverse_idx("HELLO", 0))
    print(reverse_idx("HELLO", 4))
    print(reverse_idx("HELLO", 6))