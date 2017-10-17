#! /usr/bin/python3

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

    def print_node(self):
        print(self.val)

class Dedequeue(Node):
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def dequeue_count(self):
        return self.count

    def dequeue_empty(self):
        return self.head == None

    def print_dequeue(self):
        print("Printing dequeue")
        if not self.dequeue_empty():
            print("Total count is {}".format(self.dequeue_count()))
            node = self.head
            while node:
                node.print_node()
                node = node.next
        else:
            print("Dequeue empty!")

    def dequeue_it(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def addFirst(self, node):
        if self.dequeue_empty():
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        
        self.head = node
        self.count += 1

    def removeFirst(self):
        if not self.dequeue_empty():
            node = self.head
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return node
        else:
            print("Dequeue empty!")
            return None

    def addLast(self, node):
        if self.dequeue_empty():
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.count += 1

    def removeLast(self):
        if not self.dequeue_empty():
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return node
        else:
            print("Dequeue empty!")
            return None

def create_node(val):
    return Node(val)

def test_dequeue():
    dequeue = Dedequeue()

    dequeue.addFirst(create_node(1))
    dequeue.addLast(create_node(2))
    dequeue.addFirst(create_node(3))
    dequeue.addLast(create_node(4))
    dequeue.addLast(create_node(5))
    dequeue.addFirst(create_node(6))
    dequeue.addFirst(create_node(7))
    dequeue.addLast(create_node(8))
    dequeue.addFirst(create_node(9))
    dequeue.addFirst(create_node(10))

    dequeue.print_dequeue()
    print()

    node = dequeue.removeLast()
    if node:
        node.print_node()
    else:
        print("Got none!")

    dequeue.print_dequeue()
    print()

    node = dequeue.removeFirst()
    if node:
        node.print_node()
    else:
        print("Got none!")

    print("Printing dequeue using iterator")
    for node in dequeue.dequeue_it():
        node.print_node()

def main():
    test_dequeue()

if __name__ == "__main__": main()

