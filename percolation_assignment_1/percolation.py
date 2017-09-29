#! /usr/bin/python3

from weighted_unionfind import WeightedUnionFind

class Percolation:
    # Static/Class variables
    full, open, close = 2, 1, 0

    # Private APIs

    #Constructor and init methods
    def __init__(self, size):
        self.init_grid(size)
        self.init_wuf(size)

    def init_grid(self, n):
        self.grid = [[Percolation.close for row in range(n)] for col in range(n)]
        self.grid_size = n
        self.top_row, self.bottom_row = 0, n-1

    def init_wuf(self, size):
        self.wuf = WeightedUnionFind(size*size)

    # Grid print methods
    def get_row_root_list(self, row, rownum):
        root_list = []
        for colnum, elem in enumerate(row):
            root_row, root_col = self.get_root_site(rownum, colnum)
            root_list.append(self.grid[root_row][root_col])
        return root_list

    def get_row_root_info(self, row, rownum):
        root_info = []
        for colnum, elem in enumerate(row):
            root_row, root_col = self.get_root_site(rownum, colnum)
            root_info.append(self.site_row_col_to_index(root_row, root_col))
        return root_info

    def print_row(self, row, rownum, printActualSite, printRootInfo):
        if not printActualSite:
            print(self.get_row_root_list(row, rownum), end='')
        else:
            print(row, end='')

        if printRootInfo:
            print("\t", end='')
            print(self.get_row_root_info(row, rownum))
            
        print()

    def print_grid(self):
        print("\nGrid")
        for rownum, row in enumerate(self.grid):
            self.print_row(row, rownum, False, False)

    def print_actual_grid(self):
        print("\nActual Grid")
        for rownum, row in enumerate(self.grid):
            self.print_row(row, rownum, True, True)

    #Utility methods
    def site_row_col_to_index(self, row, col):
        return row*self.grid_size + col
    
    def site_index_to_row_col(self, index):
        return index//self.grid_size, index%self.grid_size

    def is_top_row_site(self, row): return row == self.top_row

    def is_site_valid(self, row, col):
        if (    row >= self.top_row     and     col >=self.top_row 
            and row <= self.bottom_row  and     col <= self.bottom_row):
            return True
        else:
            return False

    def number_of_open_sites(self): return sum(row.count(Percolation.open) for row in self.grid)

    def get_root_site(self, row, col):
        if self.is_site_valid(row, col):
            index = self.site_row_col_to_index(row, col)
            root_index = self.wuf.find(index)
            return self.site_index_to_row_col(root_index)

    def full_site(self, row, col): self.grid[row][col] = Percolation.full

    def full_root_site(self, row, col):
        root_row, root_col = self.get_root_site(row, col)
        self.full_site(root_row, root_col)

    def update_neighbor_sites_root_fullness(self, row1, col1, row2, col2):
         if self.is_site_full(row1, col1):
             self.full_root_site(row2, col2)
         elif self.is_site_full(row2, col2):
             self.full_root_site(row1, col1)

    def connect_neighbor_sites(self, row1, col1, row2, col2):
        if self.is_site_open(row1, col1) and self.is_site_open(row2, col2):
            self.update_neighbor_sites_root_fullness(row1, col1, row2, col2)
            index1 = self.site_row_col_to_index(row1, col1)
            index2 = self.site_row_col_to_index(row2, col2)
            self.wuf.union(index1, index2)

    def connect_neighbors(self, row, col):
        self.connect_neighbor_sites(row, col, row-1, col)
        self.connect_neighbor_sites(row, col, row, col-1)
        self.connect_neighbor_sites(row, col, row, col+1)
        self.connect_neighbor_sites(row, col, row+1, col)

    def is_root_site_full(self, row, col):
        if self.is_site_valid(row, col):
            root_row, root_col = self.get_root_site(row, col)
            return self.grid[root_row][root_col] == Percolation.full
    
    # public APIs
    def is_site_open(self, row, col): return self.is_site_valid(row, col) and self.grid[row][col] > Percolation.close

    def is_site_full(self, row, col): return self.is_root_site_full(row, col)
  
    def open_site(self, row, col):
        if self.is_site_valid(row, col):
            self.grid[row][col] = Percolation.open
            if self.is_top_row_site(row):
                self.full_site(row, col)
            self.connect_neighbors(row, col)

    def percolates(self):
        for colnum, col in enumerate(self.grid[self.bottom_row]):
            if self.is_site_full(self.bottom_row, colnum): return True
        else:
            return False

def MonteOpen(grid, row, col):
    print("\nOpening site ({},{})".format(row, col))
    grid.open_site(row, col)
    grid.print_grid()

def MonteRandomSimulate(grid):
    '''
    MonteOpen(grid,0,3)
    MonteOpen(grid,2,3)
    MonteOpen(grid,2,4)
    MonteOpen(grid,1,4)
    MonteOpen(grid,1,3)
    MonteOpen(grid,4,1)
    MonteOpen(grid,3,2)
    MonteOpen(grid,3,3)
    MonteOpen(grid,4,2)
    '''

    MonteOpen(grid,1,0)
    MonteOpen(grid,1,1)
    MonteOpen(grid,1,2)
    MonteOpen(grid,2,0)
    MonteOpen(grid,2,1)
    MonteOpen(grid,2,2)
    MonteOpen(grid,3,0)
    MonteOpen(grid,3,1)
    MonteOpen(grid,3,2)
    #MonteOpen(grid,4,0)
    #MonteOpen(grid,4,1)
    MonteOpen(grid,4,2)

    MonteOpen(grid,0,4)
    MonteOpen(grid,1,4)
    MonteOpen(grid,2,4)
    MonteOpen(grid,3,4)

    MonteOpen(grid,3,3)

def MonteCarloSimulate(n):
    grid = Percolation(n)
    grid.print_grid()

    MonteRandomSimulate(grid)

    grid.print_actual_grid()

    if grid.percolates():
        print("Grid percolates")
    else:
        print("Grid does not percolate")

def main():
    n = 5
    MonteCarloSimulate(n)

if __name__ == "__main__": main()
