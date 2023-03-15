# Without min or max function and index function

def sort_by_ascending(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):  # -1 because the last element will already be the last

        min_index = i

        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[min_index] > list_of_numbers[j]:
                min_index = j

        if list_of_numbers[i] != list_of_numbers[min_index]:  # If the min its already in its position then do nothing otherwise ...
            list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]

    print(list_of_numbers)


def sort_by_descending(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):  # -1 because the last element will already be the last

        max_index = i

        for j in range(i + 1, len(list_of_numbers)):
            if list_of_numbers[max_index] < list_of_numbers[j]:
                max_index = j

        if list_of_numbers[i] != list_of_numbers[max_index]:  # If the min its already in its position then do nothing otherwise ...
            list_of_numbers[i], list_of_numbers[max_index] = list_of_numbers[max_index], list_of_numbers[i]

    print(list_of_numbers)


sort_by_ascending([56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21])
sort_by_descending([56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21])
