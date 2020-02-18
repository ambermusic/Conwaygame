from random import randint


class ConwayGame:
    def __init__(self, n):
        self.grid = []
        self.n = n
        self.zeros()

    def __str__(self):
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
        self.grid = [[0 for j in range(self.n)] for i in range(self.n)]

    def randomize(self):
        self.grid = [[randint(0, 1) for j in range(self.n)] for i in range(self.n)]

    def next_conway(self):
        n = self.n
        next_grid = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                neighbors = self.count_neighbors(i, j)
                if (self.grid[i][j] == 0) and (neighbors == 3):
                    next_grid[i][j] = 1
                if (self.grid[i][j] == 1):
                    if (neighbors < 4) & (neighbors > 1):
                        next_grid[i][j] = 1
        self.grid = next_grid

    def count_neighbors(self, i, j):
        n = self.n
        count = 0
        for k in range(i - 1, i + 2):
            for m in range(j - 1, j + 2):
                count += self.grid[k % n][m % n]
        count -= self.grid[i][j]
        return count

    def flip_square(self, row, col):
        if (0 <= row < self.n) and (0 <= col < self.n):
            self.grid[row][col] = 1 - self.grid[row][col]
