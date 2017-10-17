#! /usr/bin/python3

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def print_node(self):
        print(self.val)

class Queue(Node):
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def queue_count(self):
        return self.count

    def queue_empty(self):
        return self.head == None

    def print_queue(self):
        print("Printing queue")
        if not self.queue_empty():
            print("Total count is {}".format(self.queue_count()))
            node = self.head
            while node:
                node.print_node()
                node = node.next
        else:
            print("Queue empty!")

    def queue_it(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def enqueue(self, node):
        if self.queue_empty():
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node
        self.count += 1

    def dequeue(self):
        if not self.queue_empty():
            node = self.head
            self.head = self.head.next
            self.count -= 1
            return node
        else:
            print("Queue empty!")
            return None

def create_node(val):
    return Node(val)

def test_queue():
    queue = Queue()

    queue.enqueue(create_node(1))
    queue.enqueue(create_node(2))
    queue.enqueue(create_node(3))
    queue.enqueue(create_node(4))
    queue.enqueue(create_node(5))
    queue.enqueue(create_node(6))
    queue.enqueue(create_node(7))
    queue.enqueue(create_node(8))
    queue.enqueue(create_node(9))
    queue.enqueue(create_node(10))
    #queue.print_queue()

    node = queue.dequeue()
    if node:
        node.print_node()
    else:
        print("Got none!")

    #queue.print_queue()

    print("Printing queue using iterator")
    for node in queue.queue_it():
        node.print_node()

def main():
    test_queue()

if __name__ == "__main__": main()
