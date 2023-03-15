# Find out the minimum value, swap the value to the 0th position, repeat until lit is completely sorted
# lista = [56, 20, 4, 8, 7, 2, 3, 311, 165, 213, 21]


def sort_by_ascending(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):  # -1 because the last element will already be the last
        min_value = min(list_of_numbers[i:])
        min_index = list_of_numbers.index(min_value,
                                          i)  # Start the index search from the i position ( to work for duplicate order )
        if list_of_numbers[i] != list_of_numbers[min_index]:  # If the min its already in its position then do nothing otherwise ...
            list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]

    print(list_of_numbers)


def sort_by_descending(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):  # -1 because the last element will already be the last
        max_value = max(list_of_numbers[i:])
        max_index = list_of_numbers.index(max_value,
                                          i)  # Start the index search from the i position ( to work for duplicate order )
        if list_of_numbers[i] != list_of_numbers[max_index]:  # If the min its already in its position then do nothing otherwise ...
            list_of_numbers[i], list_of_numbers[max_index] = list_of_numbers[max_index], list_of_numbers[i]

    print(list_of_numbers)


# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
