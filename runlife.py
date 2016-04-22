import Tkinter
import sys
from gol import Life
import util

# runlife.py
# Jeff Jacobs, for CS221

boardFile = sys.argv[1]

game = Life(util.loadBoard(boardFile))

root = Tkinter.Tk()
root.wm_title("Life!!!")

cells = [[0 for x in range(game.rows)] for y in range(game.cols)]

for r in range(game.rows):
    for c in range(game.cols):
        alive = game.isAlive(r, c)
        color = ""
        if alive:
            color = "white"
        else:
            color = "black"
        cells[r][c] = Tkinter.Canvas(root, background=color, width=12, height=12, borderwidth=0)
        cells[r][c].grid(row=r, column=c)


def animate():
    updateBoard()
    game.runTimeStep()
    # 500 here controls the cpu time in ms between timesteps
    root.after(500, animate)


def updateBoard():
    for r in range(game.rows):
        for c in range(game.cols):
            alive = game.isAlive(r, c)
            color = ""
            if alive:
                color = "white"
            else:
                color = "black"
            cells[r][c].configure(background=color)

animate()
root.mainloop()
