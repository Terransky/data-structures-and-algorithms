# Stacks and Queues
Challenge that has a Stack and Queue class with methods that push, pop, enqueue, and dequeue
respectively. Both classes have their own individual peek and is_empty methods.

## Challenge
Stacks should, like a stack of plates, add to the top and take from the top in a FILO and LIFO
fashion.
Queues should, like a supermarket line, add to the rear and take from the front in a FIFO and LILO
fashion.

## Approach & Efficiency

### Approach
Start by creating a node class.
Then give the Stack and Queue class a corresponding self.head, self.top and self.front in this case
to mark the beginning of the linked list. Then make methods that traverse the linked lists
accordingly and place the node in their rightful place.

### Time and Space Complexity
Time is O(1) because regardless of input, time for traversal is either the top/front or bottom/rear
Space is O(1) generally but may be O(n) when we push or enqueue since we are increasing memory demand
based on variable user input.
