# from data_structures.stack import Stack
from python.stacks_and_queues.cc10.cc10 import Stack

class PseudoQueue:
    """"""
    def __init__(self):
        pass

    def enqueue(self, value):
        """inserts node with new value using FIFO approach"""
        # use 2 stacks to put node at front of queue instead of rear
        pass

    def dequeue(self):
        """extracts a value from the queue and removes node using a FIFO approach"""
        # use 2 stacks to return the rear rather than the front

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    print("")
