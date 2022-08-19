# Challenge Summary
Write a blog post on Insertion Sort.

```
FOR i = 1 to arr.length

  int j <-- i - 1
  int temp <-- arr[i]

```
Using this as our example list:
example = [3, 2, 1, 0]

For the entire length of a list
j always starts -1 to i and temp equals the value at index [i], which is -1 to start

while j is a positive integer (going negative breaks the while loop) and
temp is less than the value at index [j] (this is what sorts it numerically)

```
  WHILE j >= 0 AND temp < arr[j]
    arr[j + 1] <-- arr[j]
    j <-- j - 1

  arr[j + 1] <-- temp
    list[j+1] = list[j]  # eg, list[2] = list[1]
    decrement j -1
    list[j+1] = temp  # eg, list[1] = list[i]
```

It will skip the first index because i = 0 and j = -1 and move on to i = 1.
Repeat the while loop to keep moving the variable temp backward to the correct position
by checking if value temp which is list[i] is less than list[j]
It will look like this step by step for one full cycle when i = 2:

i = 2, j = 1, example = [2, 3, 1, 0]
i = 2, j = 0, example = [2, 1, 3, 0]
i = 2, j = -1, example = [1, 2, 3, 0]

and the while loop breaks and will move to the next cycle to move the 0 to front of the list


## Approach & Efficiency
Time complexity of O(n) because it must run through the entire list once regardless of whether it's sorted.
Space of O(1) because we mutate the data in place.

## Solution
```
def insertion_sort(int_list):

    if isinstance(int_list, list) is not True:
        return "Please input a list"

    for i in range(1, len(int_list)):

        j = i - 1
        temp = int_list[i]

        while j >= 0 and temp < int_list[j]:
            int_list[j+1] = int_list[j]
            j -= 1

            int_list[j + 1] = temp

    return int_list
```
