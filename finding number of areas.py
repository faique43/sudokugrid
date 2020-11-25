import math
sudokuGrid = [
[0,0,0,1],
[0,2,0,0],
[0,0,4,0],
[3,0,0,0]
]
size = len(sudokuGrid)
print("Sudoku grid size is ", size, " by ", size)
for row in range(size):
    print (sudokuGrid[row])
area = int(math.sqrt(size))
print ("Size of each area is: ", area, " by ",area)
