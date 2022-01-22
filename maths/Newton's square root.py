

def sqrt(n):
    x = n
    while True:
        root = 0.5 * (x+(n/x))

        if abs(root-x) < 1:
            break
        else:
            x = root
    return root


print(sqrt(40))
