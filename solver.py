from sudoku import *

s = Sudoku()
#s.show()

def mark(x, y, n, sudoku=s.grid):
    if n in sudoku[y][x]:
        sudoku[y][x] = [n]
    else:
        print("Invalid number/Position. No number there")
    #Remove the number from row
    for i in range(9):
        if len(sudoku[i][x]) != 1:
            sudoku[i][x].remove(n)
    #Remove the number from column
    for i in range(9):
        if len(sudoku[y][i]) != 1:
            sudoku[y][i].remove(n)
    


def check(sudoku):
    print("stuff")

mark(0, 0, 1)
mark(1, 1, 2)
print(s.grid)
print()
print(s.show())