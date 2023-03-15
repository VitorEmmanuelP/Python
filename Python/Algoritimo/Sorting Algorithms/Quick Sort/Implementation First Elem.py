# https://joaoarthurbm.github.io/eda/posts/quick-sort/
def pivot_place(list_of_numbers, first_index, last_index):
    """ to het the correct position of the pivot element"""

    pivot = list_of_numbers[first_index]
    left = first_index + 1
    right = last_index
    while True:

        while left <= right and list_of_numbers[left] <= pivot:  # To get in the descending order just change <= to >=
            left += 1

        while left <= right and list_of_numbers[right] >= pivot:  # To get in the descending order just change <= to >=
            right -= 1

        if right < left:
            break

        else:
            list_of_numbers[left], list_of_numbers[right] = list_of_numbers[right], list_of_numbers[left]

    list_of_numbers[first_index], list_of_numbers[right] = list_of_numbers[right], list_of_numbers[first_index]
    return right


def quicksort(list_of_numbers, first_index, last_index):
    if first_index < last_index:
        p = pivot_place(list_of_numbers, first_index, last_index)
        quicksort(list_of_numbers, first_index, p - 1)
        quicksort(list_of_numbers, p + 1, last_index)


# main

lista = [56, 26, 93, 17, 31, 44]
quicksort(lista, 0, len(lista) - 1)
print(lista)

