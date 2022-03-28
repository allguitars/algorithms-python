""" https://www.youtube.com/watch?v=byHi41L9vTM&ab_channel=DerrickSherrill """


def insertion_sort(list_a):
    """ inserttion sort"""
    indexing_range = range(1, len(list_a))

    for i in indexing_range:
        value_to_insert = list_a[i]

        while list_a[i-1] > value_to_insert and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i - 1

    return list_a


sample_input = [8, 7, 5, 6, 4, 1, 2, 8, 9, 5, 6, 4, 7, 8, 9]

print(insertion_sort(sample_input))
