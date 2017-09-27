#! /usr/bin/python3

#grid
class Percolation:
    open, close = 1, 0

    def __init__(self, size):
        self.init_grid(size)

    def print_grid(self):
        for i in self.grid:
            print(i)

    def init_grid(self, n):
        self.grid = [[Percolation.close for i in range(n)] for j in range(n)]
        self.grid_size = n
        print("grid created")

    def is_site_valid(self, i, j):
        if i < self.grid_size and j < self.grid_size:   return True
        else:                                           return False

    def is_site_open(self, i, j):
        if self.is_site_valid(i, j): return self.grid[i][i] == Percolation.open

    def open_site(self, i, j):
        if self.is_site_valid(i, j): self.grid[i][j] = Percolation.open

    def number_of_open_sites(self):
        return sum(i.count(1) for i in self.grid)

def main():
    grid = Percolation(10)
    grid.print_grid()
    print("grid size is {}".format(grid.grid_size))
    i, j = 3, 3
    print("site {},{} is ".format(i, j))
    print("open" if grid.is_site_open(i,j) else "closed")

    grid.open_site(i, j)
    grid.open_site(5, 5)
    print("site {},{} is ".format(i, j))
    print("open" if grid.is_site_open(i,j) else "closed")

    grid.print_grid()

    print("Number of open sites is {}".format(grid.number_of_open_sites()))


if __name__ == "__main__": main()
