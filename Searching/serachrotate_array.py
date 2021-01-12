def searchrotate_array(arr,x):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low+high) //2
        print("mid",low,high)
        if arr[mid] == x:
            return mid
        if arr[low] < arr[mid]:
            if arr[low] <= x and x <arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] < x and x< arr[high]:
                low = mid+1
            else:
                hig = mid-1
        return -1
    
arr = [10,20,40,60,5,8]
print(searchrotate_array(arr,6))
