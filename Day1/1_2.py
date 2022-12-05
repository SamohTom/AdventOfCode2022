def main():
    data = []
    final = []
    with open("Day1/input.txt") as my_file:
        my_file = my_file.read().split("\n\n")
        data = list(map(lambda x: x.split("\n"), my_file))
    
    for elf in data:
        calories = 0
        for food in elf:
            calories += int(food)
        final.append(calories)
    
    final.sort(reverse= True)

    print(sum(final[0:3]))

if __name__ == "__main__":
    main()