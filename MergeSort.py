import math
# TODO fix merge sort implementation for some reason the same obj is remade in every spot


def MergeSort(data_list):
    if len(data_list) <= 1:
        return data_list

    size = math.ceil(len(data_list) / 2)

    sublist_a = []
    sublist_b = []

    for i in range(size):
        sublist_a.append(data_list[i])

    for i in range(len(data_list) - size):
        sublist_b.append(data_list[i + size])

    sublist_a = MergeSort(sublist_a)
    sublist_b = MergeSort(sublist_b)

    return Merge(sublist_a, sublist_b)


def Merge(list_a, list_b):
    result = []
    while len(list_a) != 0 and len(list_b) != 0:
        if list_a[0].get_distance() < list_b[0].get_distance():
            result.append(list_a[0])
            del list_a[0]
        else:
            result.append(list_b[0])
            del list_b[0]

    while len(list_a) > 0:
        result.append(list_a[0])
        del list_a[0]

    while len(list_b) > 0:
        result.append(list_b[0])
        del list_b[0]

    return result
