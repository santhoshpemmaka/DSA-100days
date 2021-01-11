def binarySearch(arr,x):
    start = 0
    mid = len(arr)//2 -1
    while start <= mid:
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            mid = mid -1
        else:
            low = mid+1
    return -1
    
arr = [10,10]
print(binarySearch(arr,10))

# Adding the recursive method

def binary_search1(arr,x,low,high):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == x:
        return mid
    if arr[mid] > x:
        return binary_search(arr,x,mid+1,high)
    else:
        return binary_search(arr,x,low,mid-1)
