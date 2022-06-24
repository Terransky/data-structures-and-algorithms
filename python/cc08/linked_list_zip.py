
def zip_lists(llist1, llist2):
    """takes two linked lists and zipper merges then, alternating node by node"""

    # sets the head of the linked lists
    current1 = llist1.head
    current2 = llist2.head

    # checks for empty heads
    if current1 is None and current2 is None:
        return None

    elif current1 is None:
        return llist2

    elif current2 is None:
        return llist1

    # loops through nodes
    while current1 and current2:
        temp1 = current1.next  # is node 1-2
        temp2 = current2.next  # is node 2-2

        current1.next = current2  # connects to node 2-1

        if temp1:  # checks if llist1 node.next exists
            current2.next = temp1  # connects to node 1-2

        current1 = temp1  # becomes node 1-2
        current2 = temp2  # becomes node 2-2

        # repeats through the rest of the nodes, going to 1-3, 2-3, 1-4, 2-4...

    return llist1
