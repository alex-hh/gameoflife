# util.py
# Jeff Jacobs, for CS221


def loadBoard(filename):
    with open(filename) as f:
        content = f.readlines()

    rows = len(content)
    cols = len(content[0].strip().split(","))
    board = [[{} for x in range(rows)] for y in range(cols)]

    for r in range(rows):
        curRow = content[r].strip().split(",")
        for c in range(cols):
            curCellInt = int(curRow[c])
            if curCellInt == 0:
                board[r][c]['alive'] = False
            else:
                board[r][c]['alive'] = True
    return board


def printBoard(life):
    board = ""
    for i in range(life.getNumRows()):
        for j in range(life.getNumCols()):
            board = board + str(life.isAlive(i, j))
        board = board + "\n"
    print board
