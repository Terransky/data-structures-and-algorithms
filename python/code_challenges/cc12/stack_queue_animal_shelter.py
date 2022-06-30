# from python.data_structures.queue import Queue


class AnimalShelter:
    """a queue for dogs and cats in a shelter"""
    def __init__(self, front=None, dogs=0, cats=0):
        self.front = front
        self.dogs = dogs
        self.cats = cats

    def enqueue(self, animal):
        """checks for node.value of "dog" or "cat" and enqueues accordingly"""
        if animal.value is 'dog' or animal.value is 'cat':
            current = self.front

            if current is None:
                self.front = animal
                return

            while current:

                if current.next is None:
                    current.next = animal  # links new node as last node
                    return

                current = current.next  # traverse the queue

    def dequeue(self, pref):
        """checks preference against node.value and returns the node"""
        """todo: need to refactor this so there isn't duplicate code"""
        try:
            current = self.front

            if (pref is 'dog' and current.value is 'dog') or (pref is 'cat' and current.value is 'cat'):

                dq_node = current  # assign node value to return it
                self.front = current.next  # sets next node as self.front
                return dq_node

            else:
                while current.value is not pref:

                    prev = current  # need this to link list after returning a node that's not the self.front
                    current = current.next
                    if current.value is pref:
                        dq_node = current  # assign node value to return it
                        prev.next = current.next  # sets next node as self.front
                        return dq_node

        except:
            print("Error: Empty Queue or pref not found")
            return None


class Dog:
    """dog node"""
    def __init__(self, value='dog', next=None):
        self.value = value
        self.next = next


class Cat:
    """cat node"""
    def __init__(self, value='cat', next=None):
        self.value = value
        self.next = next
