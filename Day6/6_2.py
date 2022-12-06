def main():
    data = ""
    with open("Day6/input.txt") as my_file:
        data = my_file.read()
    
    diffRange = 14

    for i in range(len(data)-diffRange):
        if len(set(data[i:i+diffRange])) == diffRange:
            print(i+diffRange)
            return

if __name__ == "__main__":
    main()