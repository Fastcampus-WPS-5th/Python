import random

DEBUG = True

source = [x for x in range(10)]
random.shuffle(source)


# source = [5,3,7,9,1]

def print_log(*args):
    if DEBUG:
        for item in args:
            print(item, end=' ')
        print('\n', end='')


def bubble_sort(source):
    print_log('Source:     ', source)
    count_exchange = 0
    count_compare = 0
    length = len(source)

    for index, i in enumerate(range(length - 1, 0, -1)):
        for j in range(i):
            count_compare += 1
            if source[j] > source[j + 1]:
                count_exchange += 1
                source[j], source[j + 1] = source[j + 1], source[j]
        print_log('Loop Result:', source)


bubble_sort(source)