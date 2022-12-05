def main():
    final = ""
    instructions = []
    inputArrays = {}
    inputArraysData = {}
    with open("Day5/input.txt") as my_file:
        inputArraysData, instructions = my_file.read().split("\n\n")

    inputArraysData = inputArraysData.split("\n")
    inputArraysData.reverse()
    
    for i in range(1, len(inputArraysData[0]), 4):
        inputArrays[inputArraysData[0][i]] = []
    
    for i in inputArraysData[1:]:
        for x in range(1, len(inputArraysData[0]), 4):
            if i[x] == " ":continue
            inputArrays[inputArraysData[0][x]].append(i[x])

    instructions = instructions.split("\n")
    instructions = list(map(lambda x: x.split(" ")[1::2], instructions))
    
    for instruction in instructions:
        count = int(instruction[0]) * -1
        von = instruction[1]
        to = instruction[2]

        x = inputArrays[von][count:]
        inputArrays[von] = inputArrays[von][:count]
        x.reverse()
        inputArrays[to] += x

    
    for i in inputArrays.values():
        final += i[-1]

    print(final)
if __name__ == "__main__":
    main()