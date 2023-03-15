# Begin with the mid_element of the whole array as a search key.
# If the value of the search key is equal to the item then return an index of the search key.
# Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
# Otherwise, narrow it to the upper half.
# Repeatedly check from the second point until the value is found or the interval is empty.

def binary_search(list_of_numbers):

    low = 0
    high = len(list_of_numbers) - 1

    found = False

    while low <= high and not found:
        mid = (low + high) // 2
        if key == list_of_numbers[mid]:
            found = True
        elif key > list_of_numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if found:
        print('Key is found')
    else:
        print('Key not in the list')


lista = [23,1,4,2,3]
# binary search must be in a sorted list
lista.sort()

key = int(input('Enter the key: '))

binary_search(lista)

