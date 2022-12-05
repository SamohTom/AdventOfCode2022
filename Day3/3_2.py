def main():
    data = []
    badge = []
    final = 0
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")

    for i in range(0, len(data), 3):
        bp1 = data[i]
        bp2 = data[i+1]
        bp3 = data[i+2]
        for letter in set(bp1):
            if letter in set(bp2) and letter in set(bp3):
                badge.append(letter)
    
    for i in badge:
        if i.isupper():
            final += ord(i) - 38
        else:
            final += ord(i) - 96

    print(final)
    


if __name__ == "__main__":
    main()
