from random import randint


class ConwayGame:
    """Contains a grid the represents a state of Conway's Game of Life
    and methods to update the grid according to the rules of that game.
    The grid takes place on a torus so that boundary rules do not need to be taken into account.
    """
    def __init__(self, n):
        """Initializes an nxn grid of game states. Defaults to dead for all rectangles."""
        self.grid = []
        self.n = n
        self.zeros()

    def __str__(self):
        """Returns the string with the 2D array of grid states."""
        s = ""
        for i in range(self.n):
            s += str(self.grid[i])
            s += "\n"
        return s

    def __iter__(self):
        self.row = 0
        self.col = 0
        return self

    def __next__(self):
        """Returns the array (i,j,state).

         Where i is the column number, j is the row, and state is 0 if
         cell (i,j) is dead and 1 if it is alive. The next cell is found using dictionary ordering on (row,col).
         That is, after cell (n-1,i) is cell (0,i+1).
         """
        temp_row = self.row
        temp_col = self.col
        if temp_col == self.n:
            self.row = 0
            self.col = 0
            raise StopIteration
        if temp_row == self.n - 1:
            self.row = 0
            self.col += 1
        else:
            self.row += 1
        return temp_row, temp_col, self.grid[temp_row][temp_col]

    def zeros(self):
        """Replaces the current grid with one containing only dead cells."""
        self.grid = [[0 for j in range(self.n)] for i in range(self.n)]

    def randomize(self):
        """Replaces the current grid with one where all cells have a 50% chance of being alive or dead."""
        self.grid = [[randint(0, 1) for j in range(self.n)] for i in range(self.n)]

    def next_conway(self):
        """Updates the grid according to the two rules of Conway's Game of Life.

        Rule 1: If a cell is dead, it becomes alive if it has exactly 3 neighbors.
        Rule 2: If a cell is alive, it dies if it has 0 or 1 neighbors or 4 or more neighbors."""
        n = self.n
        next_grid = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                neighbors = self.count_neighbors(i, j)
                # Rule 1 implementation
                if (self.grid[i][j] == 0) and (neighbors == 3):
                    next_grid[i][j] = 1
                # Rule 2 implementation
                if (self.grid[i][j] == 1):
                    if (neighbors < 4) and (neighbors > 1):
                        next_grid[i][j] = 1
        self.grid = next_grid

    def count_neighbors(self, i, j):
        """Returns the number of alive neighbors at cell (i,j)"""
        n = self.n
        count = 0
        for k in range(i - 1, i + 2):
            for m in range(j - 1, j + 2):
                # The k % n code makes the grid update on a torus where the line bottom the bottom of the grid
                # is the top line and the line to the right of the rightmost column is the left column.
                count += self.grid[k % n][m % n]
        count -= self.grid[i][j]
        return count

    def flip_square(self, row, col):
        """Changes the state of the square at position (row,col)."""
        if (0 <= row < self.n) and (0 <= col < self.n):
            self.grid[row][col] = 1 - self.grid[row][col]
