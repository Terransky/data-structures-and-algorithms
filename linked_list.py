
class Node:
    """initializes an object with keys for value, next, and previous node"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    # def __repr__(self):
    #     return f"{self.data}"


class LinkedList:
    """maintains the linked list methods to maneuver nodes"""

    def __init__(self):
        self.head = None

    def insert(self, node):
        node.next = self.head
        self.head = node

    def append(self, value):
        """appends value to end of linked list"""
        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current:
                current = current.next
                print("test", current.next)
                if current.next is None:
                    current.next = node
                    break




    def insert_before(self, value, new_value):
        pass

    def insert_after(self, value, new_value):
        pass

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                print(f"Found it: {current.data}")
                return True
            current.head = current.next

    def to_string(self):
        current = self.head
        nodes = []

        while current is not None:
            nodes.append(f"{ {current.data} }")
            current = current.next
        nodes.append("NULL")
        return " -> ".join(nodes)

    #  formatted as "{ a } -> { b } -> { c } -> NULL"


class TargetError:
    pass


if __name__ == "__main__":

    l_list = LinkedList()

    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print(node1.data)
    print(node1.next.data)
    print(node2.next.data)
    print(node3.next.data)
    print(node4.next.data)
    print()

    l_list.head = node1
    print(l_list.head.data)

    node0 = Node("0")
    l_list.insert(node0)
    print(l_list.head.data)

    l_list.append('8')

    print(l_list.to_string())



    #  .includes() runs infinite




