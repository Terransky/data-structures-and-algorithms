# Stack Queue Animal Shelter
An animal shelter queue that accepts dogs and cats and dequeues by preference, not just FIFO

## Challenge
The Animal Shelter class method needs enqueue and dequeue methods that can check the value of the
node, dog or cat in this case, and traverse past and return the appropriate node while maintaining
linked list integrity.

## Whiteboard Process
![Whiteboard](something.jpg)
I need to vomit a couple times before I can stomach doing this.

## Approach & Efficiency

### Approach
In the class methods, use conditional statements that check if the node.value is the same as the
preference passed in. If not, traverse past. If match, return node, and link previous node to next.

### Time and Space Complexity
Time is O(1) because regardless of input, time for traversal is either the top/front or bottom/rear
Space is O(1) generally but may be O(n) when we push or enqueue since we are increasing memory demand
based on variable user input.
