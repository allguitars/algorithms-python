""" https://www.youtube.com/watch?v=g_xesqdQqvA&ab_channel=DerrickSherrill """


def bubble_sort(list_a):
    """ bubble sort """
    indexing_legth = len(list_a) - 1
    is_sorted = False
    print(list_a)

    while not is_sorted:
        is_sorted = True

        # If the list is still unsorted, start scanning from the head again.
        for i in range(0, indexing_legth):
            print(f'Comparing item[{i}]({list_a[i]}) and item[{i+1}]({list_a[i+1]})')

            if list_a[i] > list_a[i+1]:
                is_sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]

            print(list_a)

    return list_a


list_in = [8, 3, 5, 10, 7]

result = bubble_sort(list_in)
print(result)
