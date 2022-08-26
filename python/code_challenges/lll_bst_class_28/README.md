# Challenge Summary
Given a linked-list, find the largest value.
Given a BST, find the largest value
All values 0 or larger, all whole numbers. (No -negatives).

## Approach & Efficiency
For a linked list, time is O(n) because it must traverse all nodes once.
Space is constant as it only returns a value.

For a binary search tree, time is O(log n) since each step down the tree eliminates the need to search half the nodes.
Space is constant because it only turns a value.

## Solution Blog Post

A linked list starts with a node designated as a head, the start point. Itself and every node after contains a value
and a following node to link to or None to denote the end of the linked list.

In order to traverse the linked list and check the value of every node, we must use a while loop.
For each node, we check its value and if it is a new highest value, save it to a temp variable.
We continue to traverse comparing values until we reach the end. In code it looks like this:

```
def largest(self):
    current = self.head
    largest_value = self.head.value

    while current:
        previous = current
        if current.value > largest_value:
            largest_value = current.value

        current = current.next

    return largest_value
```

So given a linked list of nodes:
{1} -> {9} -> {3} -> {14}

```
# 1st node, set self.head.value to variable
largest_value = 1
# 2nd node, 9 > 1
largest_value = 9
# 3rd node, 3 < 9
largest_value = 9
# 4th node, 14 > 9
largest_value = 14
current.next = None
# exit while loop, return largest_value
```

For a binary search tree to work, it must be already sorted and each node must contain a left and a right.
For this example, the lowest values with be on the left side and the highest on the right.
As before, we start with the top level node and store its value to a variable.
As we traverse the tree, we compare left and right and overwrite that value as necessary until we reach the end.

Given a binary tree of:

           {10}
           /  \
        {9}   {11}
        /\     /\
      {3}{5} {12}{15}

```
# First we store the value of the top level node.
largest_value = self.top.value
# Then we compare that value to the left.value and the right.value.
largest_value < current.right.value
# The right.value is higher so:
largest_value = current.right.value
current = current.right
# largest_value is now equal to 11, then we compare the left and right again
largest_value < current.right.value
current = current.right
# we update the value again
# while current.left or current.right will become false and exit the loop, returning the largest value
```
