# Without min or max function

def sort_by_ascending(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):  # -1 because the last element will already be the last

        min_value = list_of_numbers[i]

        for j in range(i + 1, len(list_of_numbers)):
            if min_value > list_of_numbers[j]:
                min_value = list_of_numbers[j]

        min_index = list_of_numbers.index(min_value,
                                          i)  # Start the index search from the i position ( to work for duplicate order )
        if list_of_numbers[i] != list_of_numbers[min_index]:  # If the min its already in its position then do nothing otherwise ...
            list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]

    print(list_of_numbers)


def sort_by_descending(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):  # -1 because the last element will already be the last

        max_value = list_of_numbers[i]

        for j in range(i + 1, len(list_of_numbers)):
            if max_value < list_of_numbers[j]:
                max_value = list_of_numbers[j]

        max_index = list_of_numbers.index(max_value,
                                          i)  # Start the index search from the i position ( to work for duplicate order )
        if list_of_numbers[i] != list_of_numbers[max_index]:  # If the min its already in its position then do nothing otherwise ...
            list_of_numbers[i], list_of_numbers[max_index] = list_of_numbers[max_index], list_of_numbers[i]

    print(list_of_numbers)


sort_by_ascending([56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21])
sort_by_descending([56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21])



