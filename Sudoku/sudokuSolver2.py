
sudoku = []
counter = 0

def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def readSudoku():
    #keywordInput = input('Please input sudoku file')

    #sudokuFile = open(keywordInput, 'r', encoding='utf8')
    sudokuFile = open('sudoku.txt', 'r', encoding='utf8')
    for line in sudokuFile:
        num = line.strip().strip("[").strip("]").split(',')
        num = [int(i) for i in num]
        sudoku.append(num)
    sudokuFile.close

def drawSudoku():
    sudString = "("
    for i in range(9):
        for j in range(9):
            sudString = sudString + str(sudoku[i][j])
            sudString = sudString + ","
    sudString = sudString.strip(",")
    sudString = sudString + ")"
    # Following code credited to KCKennyLau
    q = lambda x, y: x + y + x + y + x
    r = lambda a, b, c, d, e: a + q(q(b * 3, c), d) + e + "\n"
    print(((r(*"╔═╤╦╗") + q(q("║ %d │ %d │ %d " * 3 + "║\n", r(*"╟─┼╫╢")), r(*"╠═╪╬╣")) + r(*"╚═╧╩╝")) % eval(
        sudString)))


readSudoku()
solveSudoku(sudoku)
drawSudoku()