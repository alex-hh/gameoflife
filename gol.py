def createEmptyGrid(rows, cols):
    return [[{'alive': False} for j in range(cols)] for i in range(rows)]


test_board = [[{'alive': False}, {'alive': True}, {'alive': False}], [{'alive': True}, {'alive': True}, {'alive': True}], [{'alive': False}, {'alive': True}, {'alive': False}]]


class Life:
    def __init__(self, board):
        # board is going to be a list of lists of dicts
        # [[{}, {}, {}], [{}, {}, {}]] has two row and three cols
        # could have a Cell class - self.grid = [[Cell(False) for j in range(cols)] for i in range(rows)]
        self.rows = len(board)
        self.cols = len(board[0])
        self.grid = board

    def isAlive(self, row, col):
        return self.grid[row][col]['alive']

    def setAlive(self, row, col, tf):
        self.grid[row][col]['alive'] = tf
        return

    def getNumLiveNeighbours(self, row, col):
        # use modular arithmetic to implement periodic boundary conditions (-1 maps to n-1)
        neighbour_coords = [(i % self.rows, j % self.cols) for i in range(row-1, row+2) for j in range(col-1, col+2)
                            if not (i == row and j == col or i > self.rows or j > self.cols) and
                            i >= -1 and j >= -1]
        return sum([int(self.isAlive(*coords)) for coords in neighbour_coords])

    def alive_next_step(self, row, col):
        tf = self.isAlive(row, col)
        live_neighbour_count = self.getNumLiveNeighbours(row, col)
        if tf:
            return live_neighbour_count in [2, 3]
        else:
            return live_neighbour_count == 3

    def runTimeStep(self):
        # in place: for row_index, row in enumerate(self.grid): for col_index, col in enumerate(row): setAlive(row_index, col_index, alive_next_step(row_index, col_index))
        self.grid = [[{'alive': self.alive_next_step(row_index, col_index)}
                     for col_index, col in enumerate(row)]
                     for row_index, row in enumerate(self.grid)]
        return
