# 1. Starting with the first element ( index = 0 ) compare the current
#    element with the next element of the list .
# 2. If the current element is greater than the next element of the
#    list swap them .
# 3. If the Current element is less than the next element , move to
#    the next element . Repeat step 1 .
# https://blog.betrybe.com/tecnologia/bubble-sort-tudo-sobre/
def sort_by_descending(list_of_numbers):
    for j in range(len(list_of_numbers) - 1):
        for i in range(len(list_of_numbers) - 1 - j):
            if list_of_numbers[i] < list_of_numbers[i + 1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]


def sort_by_ascending(list_of_numbers):
    for j in range(len(list_of_numbers) - 1):
        for i in range(len(list_of_numbers) - 1 - j):
            if list_of_numbers[i] > list_of_numbers[i + 1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]


# lista = [5616,51,651,65,6,68]
# With inputs
num = int(input('How many numbers do you want to enter: '))
lista = [int(input('Enter number:')) for x in range(num)]

sort_by_ascending(lista)
sort_by_descending(lista)
