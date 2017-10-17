#! /usr/bin/python3

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def print_node(self):
        print(self.val)

class Stack(Node):
    def __init__(self):
        self.count = 0
        self.top = None

    def stack_count(self):
        return self.count

    def stack_empty(self):
        return self.top == None

    def print_stack(self):
        print("Printing stack")
        if not self.stack_empty():
            print("Total count is {}".format(self.stack_count()))
            node = self.top
            while node:
                node.print_node()
                node = node.next
        else:
            print("Stack empty!")

    def stack_it(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def push(self, node):
        if not self.stack_empty():
            node.next = self.top
        
        self.top = node
        self.count += 1

    def pop(self):
        if not self.stack_empty():
            node = self.top
            self.top = self.top.next
            self.count -= 1
            return node
        else:
            print("Stack empty!")
            return None

def create_node(val):
    return Node(val)

def test_stack():
    stack = Stack()

    stack.push(create_node(1))
    stack.push(create_node(2))
    stack.push(create_node(3))
    stack.push(create_node(4))
    stack.push(create_node(5))
    stack.push(create_node(6))
    stack.push(create_node(7))
    stack.push(create_node(8))
    stack.push(create_node(9))
    stack.push(create_node(10))
    #stack.print_stack()

    node = stack.pop()
    if node:
        node.print_node()
    else:
        print("Got none!")

    #stack.print_stack()

    print("Printing stack using iterator")
    for node in stack.stack_it():
        node.print_node()

def main():
    test_stack()

if __name__ == "__main__": main()

