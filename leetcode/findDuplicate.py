

# https://leetcode.com/problems/find-the-duplicate-number/

# https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/

def findDuplicate(arr):
    i = 0
    while i < len(arr):
        correct = arr[i]-1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1

    for j in range(0, len(arr)):
        if arr[j] != j+1:
            return arr[j]


arr = [1, 3, 4, 2, 2]
findDuplicate(arr)
print(arr)
print(findDuplicate(arr))
