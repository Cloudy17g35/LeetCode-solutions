def bubble_sort(my_list):
    length_of_list = len(my_list)
    for i in range(length_of_list):  # iterating over range between 0 and length of the list -1
        for j in range(0, length_of_list - i - 1):

            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


def binary_search(my_list, target):

    #  low and high will keep track of which part of the list you'll search in
    low = 0
    high = len(my_list) - 1

    while low <= high:  # while it's not narrowed down to one element
        mid = (low + high) // 2  # setting index of middle point
        guess = my_list[mid]  # setting the guess

        if guess == target:  # if guess is the same as target
            return mid
        if guess > target:  # guess is too high
            high = mid - 1
        if guess < target:  # guess is to low
            low = mid + 1

    return None


def quicksort(my_list):

    if len(my_list) < 2:  # base case: empty array or array with one element is already sorted
        return my_list

    pivot = my_list[0]  # recursive case

    # sub-array of elements less than pivot or equal to pivot
    less_or_equal_to_pivot = [number for number in my_list[1:] if number <= pivot]

    # sub-array of elements greater than pivot
    more_than_pivot = [number for number in my_list[1:] if number > pivot]

    return quicksort(less_or_equal_to_pivot) + [pivot] + quicksort(more_than_pivot)


