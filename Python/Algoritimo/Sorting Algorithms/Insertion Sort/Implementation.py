# Consider the first element sorted, take the thirst element of the unsorted (u1) and compare with the sorted part (s1)
# If u1 < s1 then insert u1 in the correct index, else leave as it is, then take next element repeat etc
# https://www.geeksforgeeks.org/insertion-sort/
def sort_by_descending(list_of_numbers):
    for index in range(1, len(list_of_numbers)):

        current_element = list_of_numbers[index]
        pos = index

        while current_element > list_of_numbers[pos - 1] and pos > 0:
            list_of_numbers[pos] = list_of_numbers[pos - 1]
            pos -= 1

        list_of_numbers[pos] = current_element

    print(list_of_numbers)


def sort_by_ascending(list_of_numbers):
    for index in range(1, len(list_of_numbers)):

        current_element = list_of_numbers[index]
        pos = index

        while current_element < list_of_numbers[pos - 1] and pos > 0:
            list_of_numbers[pos] = list_of_numbers[pos - 1]
            pos -= 1

        list_of_numbers[pos] = current_element

    print(list_of_numbers)


# lista = [2,4,3,5,1]

# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
