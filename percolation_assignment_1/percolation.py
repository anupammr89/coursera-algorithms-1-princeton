#! /usr/bin/python3

from weighted_unionfind import WeightedUnionFind
import random
import statistics
import math

class Percolation:
    # Static/Class variables
    full, open, close = 2, 1, 0

    # Private APIs

    # Constructor and init methods
    def __init__(self, size):
        self.init_grid(size)
        self.init_wuf(size)

    def init_grid(self, n):
        self.grid = [[Percolation.close for row in range(n)] for col in range(n)]
        self.grid_size = n
        self.top_row, self.bottom_row = 0, n-1
        self.blocked_sites = set([i for i in range(n*n)])

    def init_wuf(self, size):
        self.wuf = WeightedUnionFind(size*size)

    # Grid print methods
    # For every site in a grid row, print state (full/open/close) of the corresponding root
    def print_row_root_state(self, row, rownum):
        for colnum, elem in enumerate(row):
            root_row, root_col = self.get_root_site(rownum, colnum)
            print(self.grid[root_row][root_col], end=' ')

    # Print state (full/open/close) of every site in a row
    def print_row_self_state(self, row, rownum):
        for elem in row:
            print(elem, end=' ')

    # For every site in a grid row, print its corresponding root in Weighted Union Find Structure
    def print_row_wuf_root(self, row, rownum):
        num_sites = self.grid_size * self.grid_size -1
        width = len(str(num_sites))
        for colnum, elem in enumerate(row):
            root_row, root_col = self.get_root_site(rownum, colnum)
            print(str(self.site_row_col_to_index(root_row, root_col)).rjust(width), end = ' ')

    # Main method to print a grid row
    def print_grid_row(self, row, rownum, printActualSite, printRootInfo):
        if not printActualSite:
            self.print_row_root_state(row, rownum)
        else:
            self.print_row_self_state(row, rownum)

        if printRootInfo:
            print("\t", end='')
            self.print_row_wuf_root(row, rownum)
            
        print()

    # Print the grid. Each site will reflect the corresponding root's state (full or not)
    def print_grid(self):
        print("\nGrid")
        for rownum, row in enumerate(self.grid):
            self.print_grid_row(row, rownum, False, False)

    # Print the grid. Each site will reflect its original state
    # This will also print the root in Weighted Union Find structure for each sites
    def print_actual_grid(self):
        print("\nActual Grid")
        for rownum, row in enumerate(self.grid):
            self.print_grid_row(row, rownum, True, True)

    # Utility methods
    def site_row_col_to_index(self, row, col):  return row*self.grid_size + col
    
    def site_index_to_row_col(self, index):     return index//self.grid_size, index%self.grid_size

    def is_top_row_site(self, row):             return row == self.top_row

    def number_of_open_sites(self):             return self.grid_size*self.grid_size - sum(row.count(Percolation.close) for row in self.grid)

    def full_site(self, row, col):              self.grid[row][col] = Percolation.full

    # Check is site (row, col) is a valid and within range
    def is_site_valid(self, row, col):
        if (    row >= self.top_row     and     col >=self.top_row 
            and row <= self.bottom_row  and     col <= self.bottom_row):
            return True
        else:
            return False

    # For a site (row, col) return its corresponding root in the Weighted Union Find structure
    def get_root_site(self, row, col):
        if self.is_site_valid(row, col):
            index = self.site_row_col_to_index(row, col)
            root_index = self.wuf.find(index)
            return self.site_index_to_row_col(root_index)

    # For a site (row, col) mark its corresponding root as "full" in the Weighted Union Find structure
    def full_root_site(self, row, col):
        root_row, root_col = self.get_root_site(row, col)
        self.full_site(root_row, root_col)

    # When connecting two neighbor sites in the grid, if one is a full site, then mark other as full too
    def update_neighbor_sites_root_fullness(self, row1, col1, row2, col2):
         if self.is_site_full(row1, col1):
             self.full_root_site(row2, col2)
         elif self.is_site_full(row2, col2):
             self.full_root_site(row1, col1)

    # Connect two neighbor sites if both are open
    def connect_neighbor_sites(self, row1, col1, row2, col2):
        if self.is_site_open(row1, col1) and self.is_site_open(row2, col2):
            self.update_neighbor_sites_root_fullness(row1, col1, row2, col2)
            index1 = self.site_row_col_to_index(row1, col1)
            index2 = self.site_row_col_to_index(row2, col2)
            self.wuf.union(index1, index2)

    # Connect neighbor sites in the grid
    def connect_neighbors(self, row, col):
        self.connect_neighbor_sites(row, col, row-1, col)
        self.connect_neighbor_sites(row, col, row, col-1)
        self.connect_neighbor_sites(row, col, row, col+1)
        self.connect_neighbor_sites(row, col, row+1, col)

    # Check if a site is full. This internally checks if its corresponding root site is full
    def is_root_site_full(self, row, col):
        if self.is_site_valid(row, col):
            root_row, root_col = self.get_root_site(row, col)
            return self.grid[root_row][root_col] == Percolation.full
    
    # public APIs
    # Check if a site is not closed i.e. it is open or full
    def is_site_open(self, row, col): return self.is_site_valid(row, col) and self.grid[row][col] > Percolation.close

    # Check if a site is full
    def is_site_full(self, row, col): return self.is_root_site_full(row, col)
  
    # Open a site
    def open_site(self, row, col):
        if self.is_site_valid(row, col):
            self.grid[row][col] = Percolation.open
            self.blocked_sites.remove(self.site_row_col_to_index(row, col))
            if self.is_top_row_site(row):
                self.full_site(row, col)
            self.connect_neighbors(row, col)

    # Check if the system percolates
    def percolates(self):
        for colnum, col in enumerate(self.grid[self.bottom_row]):
            if self.is_site_full(self.bottom_row, colnum): return True
        else:
            return False

class PercolationStats:
    # Private APIs

    # Constructor and init methods
    def __init__(self, grid_size, num_experiments):
        self.grid_size = grid_size
        self.num_experiments = num_experiments  
        self.num_open_sites_when_percolates = []
        self.MonteCarloSimulate()
        self.printStats()

    def MonteCarloSimulate(self):
        for i in range(self.num_experiments):
            self.grid = Percolation(self.grid_size)
            open_sites = self.RunMonteCarloSimulation()
            self.num_open_sites_when_percolates.append(open_sites)

    def RunMonteCarloSimulation(self):
        #self.grid.print_grid()
        #self.grid.print_actual_grid()

        while(self.grid.percolates() != True):
            self.GridOpenRandomSite(self.grid)

        #self.grid.print_grid()
        #self.grid.print_actual_grid()

        fraction = self.grid.number_of_open_sites()/(self.grid_size*self.grid_size)
        print("Number of open/full sites is {}".format(fraction))

        return fraction

    def GridOpenRandomSite(self, grid):
        random_index = random.sample(self.grid.blocked_sites, 1)
        row, col = self.grid.site_index_to_row_col(random_index[0])
        self.GridOpen(self.grid, row, col)

    def GridOpen(self, grid, row, col):
        #print("\nOpening site ({},{})".format(row, col))
        grid.open_site(row, col)
        #grid.print_grid()
        #grid.print_actual_grid()

    def mean(self):
        return statistics.mean(self.num_open_sites_when_percolates)

    def variance(self):
        return statistics.variance(self.num_open_sites_when_percolates)

    def stddev(self):
        return statistics.stdev(self.num_open_sites_when_percolates)

    def confidenceLow(self):
        return self.mean() - (1.96*self.stddev()/math.sqrt(self.grid_size))

    def confidenceHigh(self):
        return self.mean() + (1.96*self.stddev()/math.sqrt(self.grid_size))

    def printStats(self):
        print("Mean - {}".format(self.mean()))
        print("Variance - {}".format(self.variance()))
        print("Standard Deviation - {}".format(self.stddev()))
        print("Confidence Low - {}".format(self.confidenceLow()))
        print("Confidence High - {}".format(self.confidenceHigh()))

def main():
    size = 10
    num = 10
    ps = PercolationStats(size, num)

if __name__ == "__main__": main()
