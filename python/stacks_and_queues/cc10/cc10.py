
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
            return self.top.value
        except:
            print("Error: Empty Stack")

    def is_empty(self):
        """returns Boolean for whether stack is empty"""
        if self.top:
            return False
        else:
            return True


class Queue:
    def __init__(self, front=None):
        self.front = front

    def enqueue(self, value):
        """adds new node with given value to rear of queue, no return"""
        new = Node(value)  # make new node with input
        current = self.front

        while current:

            if current.next is None:
                current.next = new  # links new node as last node
                return

            current = current.next  # traverse the queue

    def dequeue(self):
        """returns the value from node at front of queue and removes it"""
        try:
            while self.front:
                dq_node_value = self.front.value  # assign node value to return it
                self.front.next = self.front  # sets next node as self.front
                return dq_node_value

        except:
            print("Error: Empty Queue")

    def peek(self):
        """returns value of the node located at front of queue"""
        try:
            return self.front.value
        except:
            print("Error: Empty Queue")

    def is_empty(self):
        """returns Boolean for whether queue is empty"""
        if self.front:
            return False
        else:
            return True


if __name__ == "__main__":

    node3 = Node(3)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    node_c = Node("c")
    node_b = Node("b", node_c)
    node_a = Node("a", node_b)

    stack = Stack(node1)
    queue = Queue(node_a)

    print(stack.top.value)
    print(stack.top.next.value)
    print(stack.top.next.next.value)

    stack.push(4)
    print(stack.top.value)

    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())

    print()

    print(queue.front.value)
    print(queue.front.next.value)
    print(queue.front.next.next.value)

    queue.enqueue('d')
    print(queue.front.next.next.next.value)

    print(queue.dequeue())
    print(queue.peek())
    print(queue.is_empty())

