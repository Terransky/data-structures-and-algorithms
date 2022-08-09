"""  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

      basically:
      for the entire length of a list
      j always starts -1 to i and
      temp equals the value at index [i]

      while j is a positive integer (going negative breaks the while loop) and
      temp is less than the value at index [j] (this is what sorts it numerically)

        list[j+1] = list[j]  # eg, list[2] = list[1]
        decrement j -1
        list[j+1] = temp  # eg, list[1] = list[i]

        repeat while loop to keep moving the variable temp backward to the correct position
      """


def insertion_sort(int_list):

    for i in range(1, len(int_list)):

        j = i - 1
        temp = int_list[i]

        while j >= 0 and temp < int_list[j]:
            int_list[j+1] = int_list[j]
            j -= 1

            int_list[j + 1] = temp

    return int_list


if __name__ == '__main__':

    unsorted_list = [5, 4, 8, 9, 3, 2, 1]
    example1 = [8,4,23,42,16,15]
    reverse = [20,18,12,8,5,-2]
    uniques = [5,12,7,5,5,7]
    nearly = [2,3,5,7,13,11]

    print(insertion_sort(unsorted_list))
    print(insertion_sort(example1))
    print(insertion_sort(reverse))
    print(insertion_sort(uniques))
    print(insertion_sort(nearly))
