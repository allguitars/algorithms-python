'''
Quick Sort - Abdul Bari
https://youtu.be/7h1s2SojIRw
Anylysis:
https://youtu.be/-qOVVRIZzao
'''


def partion(lst, l, h):
    '''
    l and h indicate the boundary of the sub-list that the
    current recursive call is dealing with.
    '''
    print(f'>>>> dealing with the partion ({l} - {h})\n')

    i, j = l, h
    pivot = lst[l]

    # while i and j is not crossing
    while i < j:
        # move both i and j towards the middle of the list until
        # we find a swappable pair (smaller one should be on the
        # left and greater one should be on the right)
        while lst[i] <= pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1

        # then swap the two numbers
        if i < j:
            print(f'swapped pair -- i: {i}, j: {j}')

            lst[i], lst[j] = lst[j], lst[i]

            print('after swapped: ', lst, '\n')
        else:
            print(f'i ({i}) and j ({j}) have crossed each other, do not swap\n')

    # place pivot in the sorted postion
    lst[l], lst[j] = lst[j], lst[l]
    print(f'place the pivot in the sorted position {j}:')
    print(lst, '\n')

    return j


def sort(lst, l, h):
    '''
    main quicksort algorithm with recursion
    '''
    if l < h:  # should have at least two elements
        j = partion(lst, l, h)
        sort(lst, l, j)
        sort(lst, j+1, h)


def quicksort(lst):
    '''
    Provides an function interface for the client.
    It gets the low and high positions and append an infinity
    number to the end of the list before calling the main algorithm.
    '''
    # don't need to sort when there is only one number
    if len(lst) > 1:
        low = 0
        high = len(lst) - 1

        lst.append(float('inf'))
        sort(lst, low, high)

    # pop out the infinity number after the sorting
    lst.pop()


SAMPLE = [10, 16, 8, 12, 15, 6, 3, 9, 5]
# SAMPLE = [20, 10]
# SAMPLE = [10, 10]   # TODO: this case is not handled

quicksort(SAMPLE)

print('\nResult:', SAMPLE)
