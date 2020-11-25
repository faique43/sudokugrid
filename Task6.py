import math
sudokuGrid = [
[0, 0, 0, 1],
[0, 2, 0, 0],
[0, 0, 4, 0],
[3, 0, 0, 0]
]
size = len(sudokuGrid)
print("Sudoku grid size is ", size, " by ", size)
for row in range(size):
    print(sudokuGrid[row])
area = int(math.sqrt(size))
print("Size of each area is: ", area, " by ", area)
for target in range(1, 5):
    row = 0
    while row < 4:
        col = 0
        while col < 4:
            print("\nChecking the following area for target value: ", target)
            print("start row: ", row)
            print("end row: ", row + area - 1)
            print("start col: ", col)
            print("end col: ", col + area - 1)
            print()
            # print ("Looking for ", target)
            foundTarget = False
            for r in range(row, row + area):
                for c in range(col, col + area):
                    # print ("Checking - Row: ", r, " Column: ", c, end="")
                    if sudokuGrid[r][c] == target:
                        # print (" - Target is already in area")
                        foundTarget = True
                        break
                    # else:
                        # print (" - Not here")
            print("The target value ", target, end="")
            if not foundTarget:
                print(" was not in area")
                l = []
                for r in range(row, row + area):
                    for c in range(col, col + area):
                        print("Checking - Row: ", r, " Column: ", c)
                        if sudokuGrid[r][c] == 0:
                            print("Square available")
                            print("Row contains", sudokuGrid[r])
                            print("Column contains", [row[c] for row in sudokuGrid])
                        else:
                            print("Square is already occupied.")
            else:
                print(" was found in area")
            col = col + 2
        row = row + 2
