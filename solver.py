from sudoku import *

s = Sudoku()
#s.show()

def mark(x, y, n, sudoku=s.grid):
    if n in sudoku[y][x]:
        sudoku[y][x] = [n]
    else:
        print("Invalid number/Position. No number there")
    #Remove the number from column
    for i in range(9):
        if len(sudoku[i][x]) != 1:
            sudoku[i][x].remove(n)
    #Remove the number from row
    for i in range(9):
        if len(sudoku[y][i]) != 1:
            sudoku[y][i].remove(n)
    #Remove the number in the 3x3 grid according to sudoku rules.
    startx = x // 3 * 3
    starty = y // 3 * 3
    for i in range(startx, startx + 3):
        for j in range(starty, starty + 3):
            if n in sudoku[j][i] and len(sudoku[i][x]) != 1:
                sudoku[j][i].remove(n)

def check(sudoku=s.grid):
    c = []
    unique = True
    #Check row
    for i in range(9):
        if len(sudoku[i] > len(set(sudoku[i]))):
            unique = False
    #Check column
    for i in range(9):
        for j in range(9):
            c.append(sudoku[i][j])
        if len(c) > len(set(c)):
            unique = False
        c.clear()

    #for i in range(9):



mark(0, 0, 1)
check()
#mark(1, 1, 2)
print(s.grid)
print()
print(s.show())