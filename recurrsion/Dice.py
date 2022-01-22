

def dice(p, target, face):
    if target == 0:
        print(p)
        return

    for i in range(1, face):
        if i <= target:
            dice(p+1, target-1, 6)


# dice("", 4, 6)


def diceList(p, target, face):
    if target == 0:
        arr = list
        arr.append(p)
        return arr
    arr = list
    for i in range(1, face):
        if i <= target:
            arr.extend(diceList(p+1, target-1, 6))
    return arr


print(diceList(1, 4, 6))
