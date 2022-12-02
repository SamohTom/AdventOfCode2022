def main():
    data = []
    final = 0
    dataDict = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }
    with open("input.txt") as my_file:
        data = my_file.read().split("\n")
    
    for match in data:
        player = match[2]
        elf = match[0]
        if dataDict[player] == dataDict[elf]:
            final += dataDict[player] + 3
        else:
            outcome = dataDict[player] - dataDict[elf]
            if (outcome == 1) or (outcome == -2):
                final += dataDict[player] +6
            else:
                final += dataDict[player]

    print(final)

if __name__ == "__main__":
    main()
