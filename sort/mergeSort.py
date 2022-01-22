a = [5, 6, 7, 8, 9, 1, 2, 3]


def mergeSort(a):
    if len(a) == 1:
        return a

    mid = len(a)//2
    left = a[0: mid]
    right = a[mid: len(a)-1]
    mergeSort(left)
    mergeSort(right)

    return merge(left, right)


def merge(a1, a2):
    mix = []
    i, j, k = 0, 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            mix[k] = a1[i]
            i += 1
        else:
            mix[k] = a2[j]
            j += 1
    k += 1
    while i < len(a1):
        mix[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        mix[k] = a2[j]
        j += 1
        k += 1

    return mix


print(mergeSort(a))
