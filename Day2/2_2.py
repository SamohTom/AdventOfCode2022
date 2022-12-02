def main():
    data = []
    final = 0
    dataDict = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
    }
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    
    for match in data:
        outcome = match[2]
        elf = dataDict[match[0]]
        
        if outcome == "X":
            if elf == 1:
                final += 3
            elif elf == 2:
                final += 1
            elif elf == 3:
                final += 2
        elif outcome == "Y":
            final += 3 + elf
        elif outcome == "Z":
            final += 6
            if elf == 1:
                final += 2
            elif elf == 2:
                final += 3
            elif elf == 3:
                final += 1

    print(final)

if __name__ == "__main__":
    main()
