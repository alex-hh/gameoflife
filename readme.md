Code implementation based on this tutorial: http://stanford.edu/~cpiech/cs221/handouts/pythonTutorial.html

#The rules of the Game of Life

###Every time step,

  1. Any living cell with two or three living neighbours survives
  2. Any other living cell dies
  3. Any dead cell with exactly three living neighbours becomes alive

#The code

gol.py contains a class which will determine the evolution of the board based on some initial configuration.

The csv files contain initial configurations designed to generate different gol patterns.

runlife.py contains a script to animate the board's evolution.

python runlife.py <board csv file>
