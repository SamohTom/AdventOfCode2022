def main():
    data = []
    final = 0
    with open("Day4/input.txt") as my_file:
        data = my_file.read().split("\n")
    for pair in data:
        a,b = pair.split(",")

        a1, a2 = a.split("-")
        b1, b2 = b.split("-")

        if  int(b1) <= int(a1) and int(a1) <= int(b2):
            final += 1
        elif  int(b1) <= int(a2) and int(a2) <= int(b2):
            final += 1
        elif  int(a1) <= int(b1) and int(b1) <= int(a2):
            final += 1
        elif  int(a1) <= int(b2) and int(b2) <= int(a2):
            final += 1

    print(final)
if __name__ == "__main__":
    main()