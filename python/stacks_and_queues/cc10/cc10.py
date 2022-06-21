
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        """assigns a new node with given value to top of stack"""
        new = Node(value)  # make new node with input
        new.next = self.top  # put old top under new top
        self.top = new  # new node becomes top reference

    def pop(self):
        """returns value of node located at top of stack and removes it"""
        try:
            temp = self.top.value
            self.top = self.top.next
            return temp
        except:
            print("Error: Empty Stack")

    def peek(self):
        """returns value of node at top of stack with no mutations"""
        try:
            return self.top.data
        except:
            print("Error: Empty Stack")

    def is_empty(self):
        """returns Boolean for whether stack is empty"""
        if self.top:
            return True
        else:
            return False


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


if __name__ == "__main__":
    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    stack = Stack(node1)

    print(stack.top.value)
    print(stack.top.next.value)
    print(stack.top.next.next.value)

    stack.push(4)
    print(stack.top.value)

    print(stack.pop())

