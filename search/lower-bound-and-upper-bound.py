from bisect import bisect_left,bisect_right

def lowerBound(arr, target):
    n = len(arr)
    l = 0
    r = n-1
    while l < r:
        mid = (l+r)//2
        if target <= arr[mid]:
            r = mid
        else:
            l = mid+1
    return l
 
def upperBound(arr, target):
    n = len(arr)
    l = 0
    r = n-1
    while l < r:
        mid = (l+r)//2
        if target < arr[mid]:
            r = mid
        else:
            l = mid+1
    return l
 
arr = [2,3,4,6,7,8]
target = 4

print(lowerBound(arr,target)) # 2
print(upperBound(arr,target)) # 3

print(bisect_left(arr,target)) # 2
print(bisect_right(arr,target)) # 3


