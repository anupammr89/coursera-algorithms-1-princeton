#! /usr/bin/python3

import random

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def print_node(self):
        print(self.val)

class Random_Queue(Node):
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def random_queue_count(self):
        return self.count

    def random_queue_empty(self):
        return self.head == None

    def print_random_queue(self):
        print("Printing random_queue")
        if not self.random_queue_empty():
            print("Total count is {}".format(self.random_queue_count()))
            node = self.head
            while node:
                node.print_node()
                node = node.next
        else:
            print("Random_Queue empty!")

    def random_queue_it(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def enqueue(self, node):
        if self.random_queue_empty():
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node
        self.count += 1

    def random_index(self):
        return random.randint(0, self.random_queue_count()-1)

    def dequeue(self):
        if not self.random_queue_empty():
            index = self.random_index()
            print("index is {}".format(index))
            node = self.head
            for i in range(index-1):
                node = node.next
            del_node = node.next
            node.next = del_node.next
            self.count -= 1
            return del_node
        else:
            print("Random_Queue empty!")
            return None

    def sample(self):
        if not self.random_queue_empty():
            index = self.random_index()
            print("index is {}".format(index))
            node = self.head
            for i in range(index-1):
                node = node.next
            sample_node = node.next
            return sample_node
        else:
            print("Random_Queue empty!")
            return None

def create_node(val):
    return Node(val)

def test_random_queue():
    random_queue = Random_Queue()

    random_queue.enqueue(create_node(1))
    random_queue.enqueue(create_node(2))
    random_queue.enqueue(create_node(3))
    random_queue.enqueue(create_node(4))
    random_queue.enqueue(create_node(5))
    random_queue.enqueue(create_node(6))
    random_queue.enqueue(create_node(7))
    random_queue.enqueue(create_node(8))
    random_queue.enqueue(create_node(9))
    random_queue.enqueue(create_node(10))
    random_queue.print_random_queue()
    print()

    print("Deleting random node ", end = "")
    node = random_queue.dequeue()
    if node:
        node.print_node()
    else:
        print("Got none!")

    sample_node = random_queue.sample()
    print("Sample node ", end = "")
    sample_node.print_node()

    print("Printing random_queue using iterator")
    for node in random_queue.random_queue_it():
        node.print_node()

def main():
    test_random_queue()

if __name__ == "__main__": main()
