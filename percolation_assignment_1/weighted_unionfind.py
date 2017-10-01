#! /usr/bin/python3

class WeightedUnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1 for i in range(size)]
        self.components = size

    def print_root(self):
        print("Root array {}, size is {}".format(self.root, len(self.root)))
        #print("Size array {}".format(self.size))

    def find(self, p):
        while(p != self.root[p]): p = self.root[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q:
            return
        if self.size[root_p] < self.size[root_q]:
            self.root[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.root[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        self.components -= 1

    def count(self):
        return self.components

def testUnion(uf, p, q):
    print("Performing union on {},{}".format(p, q))
    uf.union(p, q)
    uf.print_root()
    print("Number of connected components is {}".format(uf.count()))

def testWeightedUnionFind():
    uf = WeightedUnionFind(10)
    uf.print_root()
    
    testUnion(uf, 4,3)
    testUnion(uf, 3, 8)
    testUnion(uf, 6, 5)
    testUnion(uf, 9, 4)
    testUnion(uf, 2, 1)
    testUnion(uf, 5, 0)
    testUnion(uf, 7, 2)
    testUnion(uf, 6, 1)
    testUnion(uf, 7, 3)

def main():
    testWeightedUnionFind()

if __name__ == "__main__": main()
