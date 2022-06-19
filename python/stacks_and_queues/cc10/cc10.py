
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        """assigns a new node with given value to top of stack"""
        pass

    def pop(self):
        """returns value of node located at top of stack and removes it"""
        # raise exception error on empty stack
        # set next node as top
        pass

    def peek(self):
        """returns value of node at top of stack with no mutations"""
        # raise exception error if None
        pass

    def is_empty(self):
        """returns Boolean for whether stack is empty"""
        pass


class Queue:
    def __init__(self, front=None):
        self.front = front

    def enqueue(self, value):
        """adds new node with given value to rear of queue, no return"""
        pass

    def dequeue(self):
        """returns the value from node at front of queue and removes it"""
        # set next node as front
        # raise exception error if None

    def peek(self):
        """returns value of the node located at front of queue"""
        # raise exception error if None

    def is_empty(self):
        """returns Boolean for whether queue is empty"""
        pass
