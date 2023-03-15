# https://www.geeksforgeeks.org/merge-sort/
def merge_sort(list_of_numbers):
    if len(list_of_numbers) > 1:
        mid = len(list_of_numbers) // 2

        left_list = list_of_numbers[:mid]
        right_list = list_of_numbers[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_of_numbers[k] = left_list[i]
                i += 1
                k += 1
            else:
                list_of_numbers[k] = right_list[j]
                j += 1
                k += 1
        while len(left_list) > i:
            list_of_numbers[k] = left_list[i]
            i += 1
            k += 1

        while len(right_list) > j:
            list_of_numbers[k] = right_list[j]
            j += 1
            k += 1


lista = [20,1,50,40,10]

merge_sort(lista)

print(lista)