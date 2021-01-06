def reverseorder(arr):
    low = 0 
    high = len(arr)-1
    while low<high:
        arr[low],arr[high] = arr[high],arr[low]
        low = low+1
        high = high-1
    return arr

print(reverseorder([10,20,30,40]))
