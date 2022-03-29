""" https://www.youtube.com/watch?v=DnvWAd-RGhk&ab_channel=DerrickSherrill """


def binary_search(sequence, item):
    """ Binary Search """

    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]

        if midpoint_value == item:
            return midpoint

        if item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1

    return None


sequence_a = [2, 3, 5, 8, 11, 13, 20, 21, 25, 30, 45]
item_a = 22

print(binary_search(sequence_a, item_a))
