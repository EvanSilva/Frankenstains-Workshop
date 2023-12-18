# https://www.codewars.com/kata/5aec1ed7de4c7f3517000079

def first_n_smallest(arr, n):

    counter = 0

    numbers_in_arr = len(arr)
    deleting_cylces = numbers_in_arr - n

    copied_list = arr [:]

    while counter < deleting_cylces:

        max_number = max(copied_list)
        copied_list.reverse()
        copied_list.remove(max_number)
        copied_list.reverse()

        counter = counter + 1

    return copied_list