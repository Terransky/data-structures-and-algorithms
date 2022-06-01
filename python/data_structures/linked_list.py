
class Node:
    """docstring"""

    def __init__(self, data):
        self.data = data
        self.next = None

    # def __repr__(self):
    #     return self.data


class LinkedList:
    """Put docstring here"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, value):
        value.next = self.head
        self.head = value

    def includes(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current.head = current.next

    def to_string(self):
        current = self.head
        nodes = []

        while current is not None:
            nodes.append(f"{ {current.data} }")
            current = current.next
        nodes.append(" -> NULL")
        return " -> ".join(nodes)

    #  formatted as "{ a } -> { b } -> { c } -> NULL"



class TargetError:
    pass


if __name__ == "__main__":

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






