""" https://www.youtube.com/watch?v=4CykZVqBuCw&ab_channel=DerrickSherrill """


def selection_sort(list_a):
    """ selection sort """
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value_index = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value_index]:  # selection sort has fewer item switches than the bubble sort
                min_value_index = j

        if min_value_index != i:
            list_a[min_value_index], list_a[i] = list_a[i], list_a[min_value_index]

    return list_a


sample_list = [5, 2, 1, 0, 5, 2, 4, 2, 9, 7, 2, 6, 8, ]
print(selection_sort(sample_list))
