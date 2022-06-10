
class Node:
    """initializes an object with keys for value, next, and previous node"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """maintains the linked list methods to maneuver nodes"""

    def __init__(self):
        self.head = None


    def insert(self, value):
        node = Node(value)
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
                if current.next is None:
                    current.next = node
                    break

    def insert_before(self, value, new_value):
        """"searches value and inserts new node with new value before found value's node"""
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node

        else:
            prev = None
            current = self.head

            while True:

                if current.data is value:  # once the value of the node matches search value
                    prev.next = new_node  # sets next of previous node to new node (inserts into link)
                    new_node.next = current  # then sets that new node's next to the node ahead
                    break

                prev = current
                current = current.next  # maintains one node ahead of prev

    def insert_after(self, value, new_value):
        """"searches value and inserts new node with new value after found value's node"""
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node

        else:
            current = self.head

            while True:

                if current.data is value:  # once the value of the node matches search value
                    new_node.next = current.next  # connects next node to new node
                    current = new_node  # inserts new node into link

                    break
                current = current.next  # traverses linked list

    def includes(self, value):
        current = self.head

        while current:
            previous = current
            if current.data == value:
                print(f"Found it: {current.data}")
                return True
            current = current.next

    def to_string(self):
        """method stores node values in list, joins them, and strips quotes from curlies"""
        current = self.head
        nodes = []

        while current is not None:
            nodes.append(f"{ {current.data} }")
            current = current.next
        nodes.append("NULL")
        str = " -> ".join(nodes)
        str = str.replace("'", ' ')  # strips quotes, preserves spacing in brackets
        return str

    def __str__(self):
        """dunder str concatenates node values and strips quotes from curlies """
        current = self.head
        str = ""

        while current is not None:
            str += f"{ { current.data } } -> "
            current = current.next
        str = str.replace("'", ' ')  # strips quotes, preserves spacing in brackets
        return str + "NULL"
        #  formatted as "{ a } -> { b } -> { c } -> NULL"


class TargetError:
    pass


if __name__ == "__main__":

    l_list = LinkedList()

    # node1 = Node("1")
    # node2 = Node("2")
    # node3 = Node("3")
    # node4 = Node("4")
    # node5 = Node("5")
    #
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    #
    # print(node1.data)
    # print(node1.next.data)
    # print(node2.next.data)
    # print(node3.next.data)
    # print(node4.next.data)
    # print()
    #
    # l_list.head = node1
    # print(l_list.head.data)
    #
    # node0 = Node("0")
    # l_list.insert(node0)
    # print(l_list.head.data)
    #
    # l_list.append('8')
    #
    # print(l_list.to_string())

    l_list.insert("apple")

    l_list.insert("banana")

    # l_list.append("cucumber")

    print(l_list.to_string())
    print(str(l_list))

    l_list.insert_before("banana", "cucumber")

    print(str(l_list))

    #  .includes() runs infinite
