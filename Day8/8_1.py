def isVisible(x, y, grid):
    if(x == 0 or y == 0 or x == len(grid[y])-1 or y == len(grid)-1):
        return True
    if max(grid[y][:x]) < grid[y][x] or max(grid[y][x+1:]) < grid[y][x]:
        return True
    transposedGrid = list(map(list, zip(*grid)))
    if max(transposedGrid[x][:y]) < transposedGrid[x][y] or max(transposedGrid[x][y+1:]) < transposedGrid[x][y]:
        return True

    return False
def main():
    data = []
    final = 0
    with open("Day8/input.txt") as my_file:
        data = my_file.read().split("\n")
        data = list(map(lambda x: list(map(lambda y: int(y),list(x))), data))



    for y in range(len(data)):
        for x in range(len(data[y])):
            visible = isVisible(x, y, data)
            if(visible):final+=1

    print(final)

if __name__ == "__main__":
    main()