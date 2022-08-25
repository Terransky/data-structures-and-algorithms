from linked_list import Node, LinkedList


class Hashtable:
    """
    A list of linked lists that handles collisions
    """

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):

        node = Node({key: value})

    def get(self):
        pass

    def contains(self):
        pass

    def keys(self):
        pass

    def hash(self):
        pass


