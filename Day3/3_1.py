def main():
    data = []
    mistakes = []
    final = 0
    with open("C:/Users/thoma/Documents/PythonProjects/AdventOfCode2022/Day3/input.txt") as my_file:
        data = my_file.read().split("\n")

    for backpack in data:
        
        compartment1 = backpack[:int(len(backpack)/2)]
        compartment2 = backpack[int(len(backpack)/2):]
        
        for i in set(compartment1):
            if i in set(compartment2):
                mistakes.append(i)

    for i in mistakes:
        if i.isupper():
            final += ord(i) - 38
        else:
            final += ord(i) - 96

    print(final)

if __name__ == "__main__":
    main()
