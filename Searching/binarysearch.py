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
