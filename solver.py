from sudoku import *

s = Sudoku()
total = 45
#s.show()

def mark(x, y, n, sudoku=s.grid):
    v = isValidRow(x, y, n, sudoku) and isValidColumn(x, y, n, sudoku) and isValid3x3(x, y, n, sudoku)
    if not v:
        return
    
    if len(sudoku[y][x]) == 1:
        print("Number already chosen")
        return
    if n in sudoku[y][x]:
        sudoku[y][x] = [n]
    else:
        print("Invalid number/Position. No number there")
    #Remove the number from column
    for i in range(9):
        if len(sudoku[i][x]) != 1 and n in sudoku[i][x]:
            sudoku[i][x].remove(n)

    #Remove the number from row
    for i in range(9):
        if len(sudoku[y][i]) != 1 and n in sudoku[y][i]:
            sudoku[y][i].remove(n)
    #Remove the number in the 3x3 grid according to sudoku rules.
    startx = x // 3 * 3
    starty = y // 3 * 3
    for i in range(startx, startx + 3):
        for j in range(starty, starty + 3):
            if n in sudoku[j][i] and sum(sudoku[j][i]) - n == 45 - n:
                sudoku[j][i].remove(n)
    print(s.show())

#Check if you can put in the column
def isValidColumn(x, y, n, sudoku):
    if n == 0:
        v = 0
        for i in sudoku[y]:
            v += sum(i)
        if v == 45:
            return True
        return False

    for i in sudoku[y]:
        if i == [n]:
            print(n, "not valid in row", x, "column ", y)
            return False
    return True

#Check if you can put in the row
def isValidRow(x, y, n, sudoku):
    if n == 0:
        for i in range(9):
            if sum(sudoku[x][i]) == 45:
                return True
        return False

    for i in range(9):
        if [n] == sudoku[x][i]:
            print(n, "not valid in row ", x, "column", y)
            return False
    return True

#Check if you can put in the 3x3 grid.
def isValid3x3(x, y, n, sudoku):
    if n == 0:
        t0 = []
        sx = x // 3 * 3
        sy = y // 3 * 3
        for i in range(sx, sx + 3):
            for j in range(sy, sy + 3):
                t0.append(sudoku[i][j])
        if sum(t0) == 45:
            return True
        return False


    t = []
    sx = x // 3 * 3
    sy = y // 3 * 3
    for i in range(sx, sx + 3):
        for j in range(sy, sy + 3):
            t.append(sudoku[i][j])
    if [n] in t:
        print(n, "not valid in 3x3 in range y:", sy, "-", sy + 3, "and x:", sx, "-", sx + 3)
        return False
    return True

def checkAll(sudoku=s.grid):
    for i in range(9):
        if not isValidRow(0, i, 0, sudoku):
            return False
        if not isValidColumn(i, 0, 0, sudoku):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isValid3x3(i, j, 0, sudoku):
                return False
    return True

"""
mark(0, 0, 1)
mark(0, 0, 1)
mark(1, 0, 1)
mark(0, 1, 1)
mark(1, 1, 1)
mark(1, 3, 1)
#mark(0, 1, 3)
#mark(2, 0, 3)
#mark(2, 0, 3)
checkAll()
#mark(1, 1, 2)
#print(s.grid)
print()
print(s.show())
"""

while(True):
    l = list(input("r c v").split())
    print(type(l[2]))
    if l[2] == "0":
        print(checkAll())
    else:
        mark(int(l[0]), int(l[1]), int(l[2]))
    