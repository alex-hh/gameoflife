# https://github.com/afrozenator/ai/blob/master/cs221/python-tutorial/gameoflife/part1/life.py


def createEmptyGrid(rows, cols):
    return [[{'alive': False} for j in range(cols)] for i in range(rows)]


test_board = [[{'alive': False}, {'alive': True}, {'alive': False}], [{'alive': True}, {'alive': True}, {'alive': True}], [{'alive': False}, {'alive': True}, {'alive': False}]]


class Life:
    def __init__(self, board):
        # board is going to be a list of lists of dicts
        # [[{}, {}, {}], [{}, {}, {}]] has two row and three cols
        self.rows = len(board)
        self.cols = len(board[0])
        self.grid = board

    def isAlive(self, row, col):
        return self.grid[row][col]['alive']

    def setAlive(self, row, col, tf):
        self.grid[row][col]['alive'] = tf
        return

    def getNumLiveNeighbours(self, row, col):
        neighbour_coords = [(i, j) for i in range(row-1, row+2) for j in range(col-1, col+2)
                            if not (i == row and j == col or i > self.rows - 1 or j > self.cols - 1) and
                            i >= 0 and j >= 0]
        return sum([int(self.isAlive(*coords)) for coords in neighbour_coords])

    def runTimeStep(self):
        pass
