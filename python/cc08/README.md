# Code Challenge 08: Zip 2 Singly Linked Lists

## Challenge Description:
Traverse through 2 lists and zipper merge them by alternately linking their node.nexts

## Whiteboard Process
![Whiteboard](https://github.com/Terransky/data-structures-and-algorithms/blob/main/python/cc08/cc08.png)

## Approach & Efficiency

### Approach
First set the heads of linked lists, save their .nexts to temporary variables for later reference,
traverse the linked lists and alternately swap their node.nexts, so 1-1 will link to 2-1, 2-1 will
link to 1-2, 1-2 will link to 2-2, and so on. Then, using our previously saved references, repeat
the cycle by setting the current node to what was once the original next nodes.

### Time and Space Complexity
Time is O(n) because we must traverse both linked lists to their respective ends given user input.
Space is O(1) because we are not using extra memory, just relinking the nodes.

## API
No API used
