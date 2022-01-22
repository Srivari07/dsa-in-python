
# Time Complexity
# worst Case: O(n)
# Best Case: O(1) -> When key is present at the middle index.

def fun(array, x):
    if len(array) == 0:
        return -1
    for i in range(0, len(array)-1):
        if array[i] == x:
            return i
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 6
print(fun(array, x))
